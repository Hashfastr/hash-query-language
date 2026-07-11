import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    from importlib import reload
    import json

    import Hql

    return Hql, Path, json, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Hql quickstart

    This notebook runs an [Hql](https://github.com/Hashfastr/Hql) query from
    Python and shows the result as a table. It uses the repo's local `json`
    example database (`local-data/tf11-so-network.json`), so it works fully
    offline — no Elasticsearch/Splunk/etc. required.

    Edit the query below and the results further down will re-run automatically.
    See `examples/notebooks/README.md` for setup instructions.
    """)
    return


@app.cell(hide_code=True)
def _(Hql, Path, mo):
    # conf/ lives at the repo root; this notebook lives two levels below it
    # (examples/notebooks/), so resolve it relative to this file rather than cwd.
    conf_dir = Path(__file__).resolve().parents[2] / "conf"

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

    conf = Hql.Config.Config(conf_dir)
    return (conf,)


@app.cell
def _():
    sigma = r'''
    title: Kalambur Backdoor Curl TOR SOCKS Proxy Execution
    id: e99375eb-3ee0-407a-9f90-79569cc6a01c
    status: experimental
    description: Detects the execution of the "curl.exe" command, referencing "SOCKS" and ".onion" domains, which could be indicative of Kalambur backdoor activity.
    references:
        - https://blog.eclecticiq.com/sandworm-apt-targets-ukrainian-users-with-trojanized-microsoft-kms-activation-tools-in-cyber-espionage-campaigns
    author: Arda Buyukkaya (EclecticIQ)
    date: 2025-02-11
    tags:
        - attack.command-and-control
        - attack.t1090
        - attack.t1573
        - attack.t1071.001
        - attack.t1059.001
        - attack.s0183
        - detection.emerging-threats
    logsource:
        category: process_creation
        product: windows
    detection:
        selection_img:
            Image|endswith: '\curl.exe'
        selection_socks:
            CommandLine|contains:
                - 'socks5h://'
                - 'socks5://'
                - 'socks4a://'
        selection_onion:
            CommandLine|contains: '.onion'
        condition: all of selection_*
    falsepositives:
        - Unlikely
    level: high
    '''
    return (sigma,)


@app.cell
def _(conf, json, sigma):
    from Hql.Parser.Sigma import SigmaParser

    # conf defined above in a collapsed cell
    parser = SigmaParser(sigma, conf)
    parser.assemble()
    if parser.assembly:
        print('Valid sigma parsed!')
    print(json.dumps(parser.assembly.to_dict()))
    return (parser,)


@app.cell
def _(conf, json, parser):
    from Hql.Compiler.Hql import HqlCompiler

    hqlcomp = HqlCompiler(conf, query=parser.assembly, hac=parser.gen_hac())
    # print(json.dumps(hqlcomp.root.recompile(conf).to_dict(), indent=2))

    print(json.dumps(hqlcomp.root.upstream[0].simple_compile(), indent=2))

    # print(hqlcomp.root.upstream[0].compiler.compile(None, prep=False))
    return


@app.cell
def _(parser):
    from Hql.Compiler.Lucene import LuceneCompiler

    lucenecomp = LuceneCompiler()
    lucenecomp.compile(parser.assembly.statements[0], prep=True)
    return


if __name__ == "__main__":
    app.run()
