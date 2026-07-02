# Python 3.14t (free-threaded) setup

Hql pins free-threaded CPython via `.python-version` (`3.14t`). `uv sync` reads
that pin and auto-installs the interpreter — you do **not** need
`uv python install 3.14t --default` (that only changes the global `python`
shim, not project resolution).

The catch is polars.

## Why polars builds from source on 3.14t

- `polars` on PyPI is a pure-Python metapackage; the compiled Rust lives in
  `polars-runtime-32` (and `polars-runtime-64` for the big-index variant).
- The runtime packages only publish `cp310-abi3` wheels. Free-threaded CPython
  does not support the stable ABI, so no published wheel matches `cp314t` —
  no free-threaded wheel has ever been released for `polars-runtime-32`.
- With no matching wheel, uv falls back to the sdist and compiles the Rust
  crate, which requires a full Rust toolchain and takes a long time.

Official free-threaded wheels are not imminent: the tracking PR
[pola-rs/polars#21914](https://github.com/pola-rs/polars/pull/21914) is a
draft, blocked on other dependencies. A third-party wheel repo exists
([harshil21/polars-runtime-32-ft](https://github.com/harshil21/polars-runtime-32-ft))
but lags behind polars releases; we self-host instead, using the same pattern.

## How this repo avoids the rebuild

We build `polars-runtime-32` wheels once for cp314t, attach them to a GitHub
Release on this repo, and point uv at them with a marker-gated source in
`pyproject.toml`:

```toml
[tool.uv.sources]
polars-runtime-32 = [
  { url = "https://github.com/Hashfastr/Hql/releases/download/polars-cp314t-<VERSION>/polars_runtime_32-<VERSION>-cp314-cp314t-manylinux_2_28_x86_64.whl", marker = "sys_platform == 'linux' and platform_machine == 'x86_64'" },
]
```

With that in place, `uv sync` installs the prebuilt wheel — no Rust toolchain
needed on dev machines.

Notes:

- Environments not matched by any marker (e.g. macOS) fall back to PyPI, which
  means an sdist build there. If you're on such a platform, build a wheel for
  it and add another entry to the list.
- There is no PEP 508 marker for free-threadedness, so the wheel applies to
  *all* linux-x86_64 syncs. That's fine because `.python-version` pins the
  project to 3.14t.
- The URL effectively pins polars to the built version. Upgrading polars means
  rebuilding the wheel, cutting a new release, and updating the URL.

## Building the wheel (maintainers)

Build on a machine with resources for a Rust compile, inside a manylinux
container so the wheel doesn't depend on the build host's glibc:

```bash
mkdir -p wheelhouse
podman run --rm -v ./wheelhouse:/out quay.io/pypa/manylinux_2_28_x86_64 bash -c '
  curl -sSf https://sh.rustup.rs | sh -s -- -y && . ~/.cargo/env
  /opt/python/cp314-cp314t/bin/python -m pip wheel polars-runtime-32==<VERSION> --no-deps -w /tmp/wh
  auditwheel repair /tmp/wh/*.whl -w /out'
```

Publish and wire up:

```bash
gh release create polars-cp314t-<VERSION> wheelhouse/*.whl \
  --title "polars-runtime-32 <VERSION> cp314t" \
  --notes "Self-built free-threaded wheels"
# update the URL in [tool.uv.sources], then:
uv lock && uv sync
```

## Verify you're actually free-threaded

If an extension module doesn't declare GIL-free support, CPython silently
re-enables the GIL when it's imported. Check:

```bash
python -W always -c "import polars, sys; print(sys._is_gil_enabled())"
```

`False` means you're running free-threaded. `True` (usually with a
`RuntimeWarning` about the GIL being enabled to load `polars.polars`) means
polars re-enabled it. You can force `PYTHON_GIL=0`, but polars' free-threading
support is unfinished upstream — expect instability if you do.

## Known non-solutions

- **Copying a venv between machines** — venvs hard-code absolute interpreter
  paths in `pyvenv.cfg` and script shebangs; they don't relocate.
- **`uv python install 3.14t --default`** — global shim only, doesn't affect
  project sync.
- **abi3 wheels from PyPI** — free-threaded CPython rejects stable-ABI wheels;
  this is why the sdist build triggers at all.
