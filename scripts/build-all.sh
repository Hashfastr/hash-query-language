#!/usr/bin/env bash
set -euo pipefail

HERE="$(dirname "$0")"

"$HERE/build-pyhql.sh"
"$HERE/build-polars.sh"
