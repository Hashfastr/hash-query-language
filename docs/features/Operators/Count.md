# count
The `count` operator counts the results for each table.
By default the `count` operator replaces all tables with data of a single row with the following schema:

```
{
    "Count": hqlt.int
}
```

If specified, the `as` clause can place the counts into it's own table.
This is a cut feature by Kusto and reimplemented here.
When specified it creates a table with the schema:

```
{
    "Table": hqlt.string,
    "Count": hqlt.int
}
```

Kusto queries with this operator are compatible with Hql and will return the same results.

```
// Counts all tables and replaces their contents with counts
Database
| count

{
    "data": {
        "big.json": [{"Count": 27786}]
    },
    "schema": {
        "big.json": {"Count": "int"}
    }
}

// Counts all tables and places contents into the _counts table
Database
| count as _counts

{
    "data": {
        "big.json": [{"agent": {"id": "47fff966-6aec-4bff-9a81-bcb24763a131"}, "metadata": {"type": "_doc", "version": "7.17.1"}}],
        "_counts": [{"Table": "big.json", "Count": 1}]
    },
    "schema": {
        "big.json": {"agent": {"id": "string"}, "metadata": {"type": "string", "version": "string"},
        "_counts": {"Table": "string", "Count": "int"}}
    }
}
```
