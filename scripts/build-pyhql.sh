#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$REPO_ROOT"

PLATFORM="${PLATFORM:-}"
IMAGE="hql-build-pyhql:local"
CONTAINER="hql-build-pyhql-tmp-$$"

mkdir -p dist

PLATFORM_ARG=()
if [[ -n "$PLATFORM" ]]; then
    PLATFORM_ARG=(--platform "$PLATFORM")
fi

echo ">>> Building pyhql wheel + sdist (platform=${PLATFORM:-native})"
podman build "${PLATFORM_ARG[@]}" -f scripts/Containerfile.pyhql -t "$IMAGE" .

echo ">>> Extracting artifacts to dist/"
podman create --name "$CONTAINER" "$IMAGE" >/dev/null
trap 'podman rm -f "$CONTAINER" >/dev/null 2>&1 || true' EXIT
podman cp "$CONTAINER:/out/." dist/

echo ">>> Done. Artifacts:"
ls -1 dist/pyhql-*.whl dist/pyhql-*.tar.gz 2>/dev/null || true
