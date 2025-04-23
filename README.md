# Hash Query Language (HQL)
Hash query language is essentially a re-implementation of [Kusto Query Language](https://github.com/microsoft/Kusto-Query-Language), Microsoft's answer to `SPL`.
This language however is exclusive to Azure solutions such as Azure Data Explorer, Log Analytics Workspaces and by extension Sentinel.
This project is an attempt at bringing this rich language to use with free alternative, such as Elasticsearch and Opensearch.

See my manifesto [here](docs/MANIFESTO.md)

## Running
Still a bit a manual process to run, doesn't return data anywhere.
You need to make a copy of `conf.json.example` to `conf.json` and configure it with your Elasticsearch instance.
This is tested with Elasticsearch 7.17, haven't tried opensearch yet.
It needs to support DSL.

You also need a container system, this was developed for and in Rocky 9.5 with podman.
It should work for others as well.

Build the containers

```
cd containers
./build.sh
```

If you use docker then just replace podman with docker.

Install deps

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Then rip it.

```
python3 Hql.py -f ./tests/tf11-simple.txt
```

This will compile out a compose file and container config files for use.
Each query set has a guid, each container has a guid.

```
./out
     /b8d1fad3
              /compose.yml
              /index-c4fb3561.json
```

Where `b8d1fad3` is the query guid, and `c4fb3561` is the container guid.
The compose then creates services named after the type of container and its guid.
The network created is also named after the query's guid.

Then running will execute the query:

```
cd ./out/b8d1fad3
podman compose up
```