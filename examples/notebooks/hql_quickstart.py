import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path

    from Hql.Config import Config
    from Hql.Helpers import run_query
    return Config, Path, mo, run_query


@app.cell
def _(mo):
    mo.md(
        """
        # Hql quickstart

        This notebook runs an [Hql](https://github.com/Hashfastr/Hql) query from
        Python and shows the result as a table. It uses the repo's local `json`
        example database (`local-data/tf11-so-network.json`), so it works fully
        offline — no Elasticsearch/Splunk/etc. required.

        Edit the query below and the results further down will re-run automatically.
        See `examples/notebooks/README.md` for setup instructions.
        """
    )
    return


@app.cell
def _(Path):
    # conf/ lives at the repo root; this notebook lives two levels below it
    # (examples/notebooks/), so resolve it relative to this file rather than cwd.
    conf_dir = Path(__file__).resolve().parents[2] / "conf"
    return (conf_dir,)


@app.cell
def _(conf_dir, mo):
    mo.stop(
        not conf_dir.is_dir(),
        mo.md(
            f"""
            **No config found at `{conf_dir}`.**

            Set one up first, from the repo root:

            ```
            cp -r conf.example conf
            ```

            Then re-run this notebook.
            """
        ).callout(kind="danger"),
    )
    return


@app.cell
def _(mo):
    query_box = mo.ui.text_area(
        value=(
            "database('json').macro('network')\n"
            "| project ['@timestamp'], src_ip=toip4(source.ip), src_port=source.port, "
            "dest_ip=toip4(destination.ip), dest_port=destination.port\n"
            "| summarize count() by src_ip"
        ),
        label="Hql query",
        full_width=True,
        rows=4,
    )
    query_box
    return (query_box,)


@app.cell
def _(Config, conf_dir, query_box, run_query):
    conf = Config(conf_dir)

    error = None
    data = None
    try:
        data = run_query(query_box.value, conf, name="notebook")
    except Exception as e:
        error = e
    return data, error


@app.cell
def _(data, error, mo):
    if error is not None:
        result = mo.md(f"**Query failed:** `{error}`").callout(kind="danger")
    elif data is None or len(data) == 0:
        result = mo.md("Query ran but returned no rows.")
    else:
        blocks = []
        for table in data:
            blocks.append(mo.md(f"**{table.name or 'Table'}** — {len(table)} rows"))
            blocks.append(mo.ui.table(table.df))
        result = mo.vstack(blocks)

    result
    return


if __name__ == "__main__":
    app.run()
