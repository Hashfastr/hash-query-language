#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$REPO_ROOT"

if ! command -v gh >/dev/null 2>&1; then
    echo "ERROR: gh CLI is not installed." >&2
    exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
    echo "ERROR: gh is not authenticated. Run 'gh auth login' first." >&2
    exit 1
fi

VERSION="$(
    awk -F' *= *' '
        /^\[project\]/ { in_project = 1; next }
        /^\[/ { in_project = 0 }
        in_project && $1 == "version" {
            gsub(/"/, "", $2); print $2; exit
        }
    ' pyproject.toml
)"

if [[ -z "$VERSION" ]]; then
    echo "ERROR: could not extract version from pyproject.toml" >&2
    exit 1
fi

TAG="v$VERSION"

shopt -s nullglob
ARTIFACTS=(dist/*.whl dist/*.tar.gz)

if [[ ${#ARTIFACTS[@]} -eq 0 ]]; then
    echo "ERROR: no artifacts in dist/. Run scripts/build-all.sh first." >&2
    exit 1
fi

if gh release view "$TAG" >/dev/null 2>&1; then
    echo "ERROR: release $TAG already exists. Bump the version in pyproject.toml." >&2
    exit 1
fi

echo ">>> Creating GitHub release $TAG with:"
printf '  %s\n' "${ARTIFACTS[@]}"

gh release create "$TAG" "${ARTIFACTS[@]}" --generate-notes --title "$TAG"
