# unnest
The `unnest` operator takes an object at the root level and 

 truncates a given set of tables to a number of results.
By default the `take` operator truncates all tables, aka pattern `*`.
Patterns can be specified using the `from` clause, with comma separated patterns.

Kusto queries containing this operator are compatible with Hql and will return the same results.

```
// Truncates all tables to 10 results
Database
| take 10

// Truncates all tables with the pattern so.beats-* to 53 results
Database
| take 53 from so.beats-*

// Truncates all tables with the patterns so.beats-* and so.network-* to 100 results
Database
| take 100 from so.beats-*, so.network-*
```
