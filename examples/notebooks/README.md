# Notebooks

This directory holds example [marimo](https://marimo.io) notebooks for exploring Hql
interactively from Python.

marimo notebooks are plain `.py` files (each cell is an `@app.cell`-decorated
function) rather than the JSON blobs Jupyter's `.ipynb` uses, so they diff
cleanly in git. marimo is also *reactive*: editing a cell automatically
re-runs every other cell that depends on it, so there's no "stale output"
problem from running cells out of order.

## Setup

From the repo root:

```
# install the notebooks dependency group (adds marimo on top of the base install)
uv sync --group notebooks

# if you haven't already set up a config (see the root README.md)
cp -r conf.example conf
```

The example notebook queries the repo's local `json` database backend, which
reads `local-data/tf11-so-network.json` (already checked into the repo), so it
runs fully offline — no Elasticsearch, Splunk, or other external service
needed.

## Running

```
# interactive editing (opens in your browser)
uv run marimo edit examples/notebooks/hql_quickstart.py

# read-only "app" view, e.g. for sharing with others
uv run marimo run examples/notebooks/hql_quickstart.py
```

## `hql_quickstart.py`

Loads the repo's `conf/` directory, exposes an editable Hql query box
(pre-filled with the same query as `examples/databases/json/json.hql`), runs
it with `Hql.Helpers.run_query`, and renders the resulting table(s). Edit the
query text and the result cell re-runs automatically.

> **Known issue:** at the time of writing, the query engine on this branch
> (`rework`) fails to compile *any* query — this is unrelated to marimo or
> this notebook. The notebook still opens and runs fine; it will just show
> the compiler's error in a callout instead of a results table until that's
> fixed.

## Writing your own

The pattern for driving Hql from Python:

```python
from pathlib import Path
from Hql.Config import Config
from Hql.Helpers import run_query

conf = Config(Path("conf"))  # repo-root conf/ directory
data = run_query("database('json').macro('network') | take 10", conf, name="my-notebook")

for table in data:
    print(table.name, table.df)       # table.df is a polars.DataFrame
    print(table.to_dicts())           # or as plain dicts, with schema applied
```
