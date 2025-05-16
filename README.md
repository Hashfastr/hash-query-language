# Hash Query Language (Hql)
Hash Query Language (Hql) is a query language designed to implement a single feature set across all database backends.
Is this accomplished by using the grammar of [Kusto Query Language](https://github.com/microsoft/Kusto-Query-Language) (KQL), a query language by Microsoft made for Azure Data Explorer, the basis for Log Analytics Workspace.
Hql seeks to provide an identical feature set for use with any backend database, enabling the use of alternative database backends such as Elasticsearch or PostgreSQL.

The inspiration of Hql comes from the frustration of using Graylog with my personal homelab after setting it up at [DEATHCON](https://deathcon.io) 2024, see [the original rant idea here](docs/MANIFESTO.md).
The implementation differs from Kusto in that it supports and embraces nosql datasets, instead of a proprietary backend structured SQL-like database.

Additionaly features unsupported by Kusto include joining datasets across different database types.
In Kusto you can join or query across databases or clusters, however only their's.
Here, the below is possible:

```
let ElasticZeek = database("tf11-elastic").index("so-network-2022.10")
| where event.module == "zeek"
| extend IPAddress = source.ip;
database("sentinel").SigninLogs
| where Username == "iamcompromised"
| project IPAddress
| join type=inner ElasticZeek on IPAddress
| summarize count() by destination.ip, destination.port, source.ip, source.port
```

In the above we found an attacker IOC in Azure, aka o365, and were able to instantly pivot to the zeek logs we have in Elasticsearch.
This is possibly the most extreme case of using the features provided.
A more common usecase could be enhancing Elasticsearch to support anything other than basic filtering.

Where a given backend does not support a given feature, such as analytic functions, it gets implemented by Hql.
Below, lines 1-3 are able to be collapsed into a single query to elastic.
It's results are returned and ingested into a [polars](https://docs.pola.rs/) DataFrame, which then the follow operations are done:

1. extend
    - A new column Hostname in the DataFrame is created with the contents of winlog.computer_name
    - Column event.code is cast to INT64 and assigned to column EventID.
2. project
    - The column EventID is fed into series_stats generating a dict with keys for each stat value.
    - Since this function is provided as the single expression, with no assigned name, it gets expanded as the new output DataFrame.

```
1 database("tf11-elastic").index("so-beats-2022.10.*")
2 | where ['@timestamp'] between ("2022-10-21T15:45:00.000Z" .. "2022-10-21T15:55:00.000Z")
3 | where winlog.computer_name == "asarea.vxnwua.net"
4 | extend Hostname = winlog.computer_name, EventID = toint(event.code)
5 | project series_stats(EventID)
```

Resulting in:

```
[{"series_stats_EventID_min": 1, "series_stats_EventID_min_idx": 105, "series_stats_EventID_max": 16394, "series_stats_EventID_max_idx": 225, "series_stats_EventID_avg": 1709.3838936669272, "series_stats_EventID_stdev": 2257.263833183075, "series_stats_EventID_variance": 5095240.012596348}]
```

## Implemented features
See the implemented features [here](docs/features/README.md).
I'll put these into issues at some point.

## Running
To run you need:

- An Elasticsearch instance (I'm using 7.17)
- Python (I'm using 3.9.21)

```
# copy and configure Hql
cp conf.json.example conf.json

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# make a query and put it into a text file
python3 Hql.py -v -f ./my-query.hql
```

Some examples are in the `tests` dir and are based on the TracerFIRE 11 dataset by Sandia National Labs.
The dataset provides Elastic logs of a series of simulated cyber attacks, perfect for this situation.