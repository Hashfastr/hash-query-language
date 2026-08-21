#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$REPO_ROOT"

if [[ -z "${UV_PUBLISH_TOKEN:-}" ]]; then
    echo "ERROR: UV_PUBLISH_TOKEN is not set." >&2
    echo "Generate a PyPI token and export it before running this script." >&2
    exit 1
fi

shopt -s nullglob
WHEELS=(dist/*.whl)
SDISTS=(dist/*.tar.gz)

if [[ ${#WHEELS[@]} -eq 0 && ${#SDISTS[@]} -eq 0 ]]; then
    echo "ERROR: no wheels or sdists found in dist/. Run scripts/build-all.sh first." >&2
    exit 1
fi

echo ">>> Publishing to PyPI:"
printf '  %s\n' "${WHEELS[@]}" "${SDISTS[@]}"

uv publish "${WHEELS[@]}" "${SDISTS[@]}"
