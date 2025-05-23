# Ingestion
The method of ingestion can differ between different database types.
This covers a common method and all database types should do some sort of variation of this.
The database here is queried and gives data as json or some other basic plain text form of data representation.
The database also gives a proper schema for how the data should be represented, or how it's represented in the database before conversion to the basic representation.

## Basic input
When queried the database gives it's basic representation, in this case json.
A schema is calculated for this dataset to ensure proper loading into polars.
This is in response to an issue with polars where the `from_dicts` method does not play well with nested structures.
When building the schema it will ensure that conflicting types are resolved to a common super type.
That is multiple rows reporting data and an integer, a float, and a string for a particular key will be all be cast to str for consistency.
Similarly, if just integers and floats, they will all be promoted to floats.
It will detect multi-value fields and unsure that all instances of that field reflect it.

Below is an example from the TF11 dataset.
Elasticsearch supports multivalues, regardless of specification by the schema.
The schema might say 'string' but really means 'string or an array of any amount of strings'.
Here 'uid' is either a string or a list of strings.
Either way they're semantically the same, so the second entry is listified.

```
{
    "id": {
        "uid": [
            "CAnltOiClThlO6ZFk"
        ],
        "fuid": "FdZyiY2Kf5yf3L4239"
    }
},
{
    "id": {
        "uid": "1017858934534263",
        "resp_fuids": None
    }
}
```

TO

```
{
    "id": {
        "uid": [
            "CAnltOiClThlO6ZFk"
        ],
        "fuid": "FdZyiY2Kf5yf3L4239"
    }
},
{
    "id": {
        "uid": [
            "1017858934534263"
        ],
        "resp_fuids": None
    }
}
```

SCHEMA

```
import HqlCompiler.Types as t
{
    "id": {
        "uid": t.multivalue(t.string),
        "fuid": t.string,
        "resp_fuids": t.null
    }
}
```

If the schema is left unspecified, then the fields 'resp_fuids' or 'fuid' might be garbaged as they are not a common field between both nested structs.
Additionally the list of the first element will be cast down to a string representation of the array, something we don't really want.

The intermediate data is then ingested into Polars with the above schema.
If a given key is missing in a row then it is evaluated as `polars.null`.

## Applying an advanced schema
The intermediate data input and schema does not account for complex field types such as `datetime` or `ip4`.
`@timestamp` is one such field which is designated as a `date` field by Elasticsearch.
In our case we can tell this by getting the index info for our data, which returns a schema for the index.
Below is the schema returned by Elasticsearch for our index, with other fields omitted.

```
{
    "so-network-2022.10": {
        "aliases": {},
        "mappings": {
            "date_detection": false,
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "@version": {
                    "type": "text",
                },
                ...
            }
        }
    }
}
```

Using this we can build out the proper target schema we can cast everything to.
For some databases this can be completely optional.

```
import HqlCompiler.Types as t
{
    "@timestamp": t.datetime,
    "version": t.string,
    ...
}
```

We can then apply the schema onto our intermediary DataFrame.
If we find a column in that DataFrame whose type differs from the type specified by the target schema, we cast it.
Depending on the kind of data the cast can be handled by polars, or handled by Hql.
An example of a cast handled by Polars is casting `int -> string`.
An example of a cast handled by Hql is casting `string (of an ip) -> UInt32`.

The target schema is then tracked with the table as it represents how some data should be displayed when exported.
So for example a IPv4 field can be converted from the UInt32 polars primative into the IPv4 text representation.

## In code
Below is a basic code representation of this taken from the `from-dicts.ipynb` notebook.
The code in the notebook might be slightly outdated or different but gets the gist across.

```
# Here json_data is the raw data returned by Elasticsearch
# This gets the actual data out and into unnested
unnested = [x['_source'] for x in json_data]

# Intermediate schema calculated
jschema = Schema(unnested)

# Adjust any values that should be multi-value before polars ingestion
# It already knows which paths were promoted so only looks for those paths
unnested = jschema.adjust_mv(unnested)

# Ingest to polars with the intermediate schema
# Invoking to_pl_schema() to convert Hql types to Polars primatives
df1 = pl.from_dicts(unnested, schema=jschema.to_pl_schema())

# Target schema
# gen_elastic_schema is a database specific function that generates an Hql schema
# based on what Elasticsearch cites.
eschema = Schema(schema=gen_elastic_schema(index['so-network-2022.10']['mappings']['properties']))

# Cast all intermediate data to target datatypes
df2 = eschema.cast_to_schema(df1)
```