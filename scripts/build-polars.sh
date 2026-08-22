#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$REPO_ROOT"

PLATFORM="${PLATFORM:-}"
IMAGE="hql-build-polars:local"
CONTAINER="hql-build-polars-tmp-$$"

# Extract polars pin from pyproject.toml (polars and polars-runtime-32 share
# a version — they are released together).
POLARS_RUNTIME_VERSION="$(
    sed -n 's/.*"polars==\([0-9][0-9.]*\)".*/\1/p' pyproject.toml | head -1
)"

if [[ -z "$POLARS_RUNTIME_VERSION" ]]; then
    echo "ERROR: could not find a 'polars==<version>' pin in pyproject.toml" >&2
    exit 1
fi

echo ">>> polars-runtime-32 pin: $POLARS_RUNTIME_VERSION (from pyproject.toml)"

mkdir -p dist

PLATFORM_ARG=()
if [[ -n "$PLATFORM" ]]; then
    PLATFORM_ARG=(--platform "$PLATFORM")
fi

# pypa manylinux images are published per-arch (no multi-arch manifest).
case "${PLATFORM:-}" in
    linux/arm64|linux/aarch64)
        BASE_IMAGE="quay.io/pypa/manylinux_2_28_aarch64" ;;
    linux/amd64|linux/x86_64|"")
        BASE_IMAGE="quay.io/pypa/manylinux_2_28_x86_64" ;;
    *)
        echo "ERROR: unsupported PLATFORM '$PLATFORM' (expected linux/amd64 or linux/arm64)" >&2
        exit 1 ;;
esac

echo ">>> Building polars-runtime-32 wheel for Python 3.14t"
echo ">>> platform=${PLATFORM:-native}  base=${BASE_IMAGE}"
echo ">>> This is a full Rust compile and will take a while."
podman build "${PLATFORM_ARG[@]}" \
    --build-arg "BASE_IMAGE=$BASE_IMAGE" \
    --build-arg "POLARS_RUNTIME_VERSION=$POLARS_RUNTIME_VERSION" \
    -f scripts/Containerfile.polars \
    -t "$IMAGE" .

echo ">>> Extracting artifacts to dist/"
podman create --name "$CONTAINER" "$IMAGE" >/dev/null
trap 'podman rm -f "$CONTAINER" >/dev/null 2>&1 || true' EXIT
podman cp "$CONTAINER:/out/." dist/

echo ">>> Done. Artifacts:"
ls -1 dist/polars_runtime_32-*.whl 2>/dev/null || true
