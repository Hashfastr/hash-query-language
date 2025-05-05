## Elastic-isms
### DSL for the _search endpoint
https://www.elastic.co/docs/reference/query-languages/querydsl

### Query Types
https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-bool-query

### SQL for elasticsearch
Probably should implement this, looks like we could do joins?

https://www.elastic.co/guide/en/elasticsearch/reference/7.17/sql-overview.html

Has a limitations section here: https://www.elastic.co/guide/en/elasticsearch/reference/7.17/sql-limitations.html

> Using sub-selects (SELECT X FROM (SELECT Y)) is supported to a small degree: any sub-select that can be "flattened" into a single SELECT is possible with Elasticsearch SQL.

Haven't tested in Kibana, but as of 2019 no such thing exists.

https://discuss.elastic.co/t/can-we-use-sql-join-in-elastic-query/196378

### Joins in elastic ES|QL
Looks like as of me working on this project ES|QL got joins... kinda...

https://www.elastic.co/blog/esql-lookup-join-elasticsearch

> Lookup Join is a SQL-style LEFT OUTER JOIN that relies on a new index mode called lookup for the right side.
> The lookup index could be assets, threat intel data like known-bad IPs, order info, employee or customer info — there are infinite possibilities.

So, not really, just left outer, and it's not a true join, seems a little hodge podged.

### Pipe operators using EQL
https://www.elastic.co/docs/reference/query-languages/eql/eql-pipe-ref

Looks like pipe operators do exist for elastic!
But you need to use EQL.
And they only support 2, head, tail, coincidentally the only ones I can implement in DSL!

## Polar
https://docs.pola.rs/api/python/stable/reference/sql/python_api.html#querying