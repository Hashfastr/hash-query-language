# Typing
Hql is a completely different query language from Kusto, and as such has different typing.
The goal of Hql is to create data representation that can spread between both structured and non-structured databases.
Essentially making a unified representation for SQL, Kusto, Elastisearch, and Splunk.

The common denominator for all of these databases is that they can be represented in json.
Since it's fairly easy to interact with as a concept, json forms the front end for the data provided by Hql.
So data going into Hql should be json serializable in some form, and the data out should also json serializable.

The vehicle for processing this generic data is Polars, a highly performant data processing engine written in rust.
Where operating on json itself is very slow, loading into a performant data structure in Polars is ultra-fast.
So many base types are handled within the constraints of the base types of Polars, thankfully there's a bunch of them.

Below are a comparison of types between Kusto, Elastic, and Hql:

| Polars                                                                                                                                                              | Hql                                                                                                                                                                   | Kusto                                                                                                        | Elastic                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Decimal`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Decimal.html#polars.datatypes.Decimal "polars.datatypes.Decimal")                 | `decimal`                                                                                                                                                             | [`decimal`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/decimal?view=microsoft-fabric)   | [`scaled_float`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)                                                                                                                                                                                     |
|                                                                                                                                                                     | Cast up to `float`                                                                                                                                                    |                                                                                                              | [`half_float`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)                                                                                                                                                                                       |
| [`Float32`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Float32.html#polars.datatypes.Float32 "polars.datatypes.Float32")                 | `float`                                                                                                                                                               |                                                                                                              | [`float`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)                                                                                                                                                                                            |
| [`Float64`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Float64.html#polars.datatypes.Float64 "polars.datatypes.Float64")                 | `double`                                                                                                                                                              | [`real`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/real?view=microsoft-fabric)         | [`double`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)                                                                                                                                                                                           |
| [`Int8`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Int8.html#polars.datatypes.Int8 "polars.datatypes.Int8")                             | `byte`                                                                                                                                                                |                                                                                                              | [`byte`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)                                                                                                                                                                                             |
| [`Int16`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Int16.html#polars.datatypes.Int16 "polars.datatypes.Int16")                         | `short`                                                                                                                                                               |                                                                                                              | [`short`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)                                                                                                                                                                                            |
| [`Int32`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Int32.html#polars.datatypes.Int32 "polars.datatypes.Int32")                         | `int`                                                                                                                                                                 | [`int`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/int?view=microsoft-fabric)           | [`integer`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)                                                                                                                                                                                          |
| [`Int64`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Int64.html#polars.datatypes.Int64 "polars.datatypes.Int64")                         | `long`                                                                                                                                                                | [`long`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/long?view=microsoft-fabric)         | [`long`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)                                                                                                                                                                                             |
| [`Int128`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Int128.html#polars.datatypes.Int128 "polars.datatypes.Int128")                     | `xlong`                                                                                                                                                               |                                                                                                              |                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                     | `guid`<br>Also a Int128 in polars, but displayed as a guid when converted to json/displayed                                                                           | [`guid`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/guid?view=microsoft-fabric)         |                                                                                                                                                                                                                                                                                    |
| [`UInt8`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.UInt8.html#polars.datatypes.UInt8 "polars.datatypes.UInt8")                         | `ubyte`                                                                                                                                                               |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`UInt16`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.UInt16.html#polars.datatypes.UInt16 "polars.datatypes.UInt16")                     | `ushort`                                                                                                                                                              |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`UInt32`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.UInt32.html#polars.datatypes.UInt32 "polars.datatypes.UInt32")                     | `uint`                                                                                                                                                                |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`UInt64`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.UInt64.html#polars.datatypes.UInt64 "polars.datatypes.UInt64")                     | `ulong`                                                                                                                                                               |                                                                                                              | [`unsigned_long`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)                                                                                                                                                                                    |
|                                                                                                                                                                     | `ip`, generic, stored as `string`                                                                                                                                     |                                                                                                              | [`ip`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/ip)                                                                                                                                                                                                   |
| [`UInt32`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.UInt32.html#polars.datatypes.UInt32 "polars.datatypes.UInt32")                     | `ip4`                                                                                                                                                                 |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`Decimal`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Decimal.html#polars.datatypes.Decimal "polars.datatypes.Decimal")                 | `ip6`                                                                                                                                                                 |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`Date`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Date.html#polars.datatypes.Date "polars.datatypes.Date")                             | Folded into `datetime`                                                                                                                                                |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`Datetime`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Datetime.html#polars.datatypes.Datetime "polars.datatypes.Datetime")             | `datetime`                                                                                                                                                            | [`datetime`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/datetime?view=microsoft-fabric) | [`date`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/date), [`date_nanos`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/date_nanos)                                                                                             |
| [`Duration`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Duration.html#polars.datatypes.Duration "polars.datatypes.Duration")             | `duration`                                                                                                                                                            |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`Time`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Time.html#polars.datatypes.Time "polars.datatypes.Time")                             | `time`, dateless                                                                                                                                                      |                                                                                                              |                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                     | `range`<br>Polars struct with a start and end datatype corresponding to the range target                                                                              |                                                                                                              |                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                     | `range` using [`Datetime`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Datetime.html#polars.datatypes.Datetime "polars.datatypes.Datetime") | [`timespan`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/timespan?view=microsoft-fabric) | [`date_range`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/range)                                                                                                                                                                                        |
|                                                                                                                                                                     | `range` using `int`                                                                                                                                                   |                                                                                                              | [`integer_range`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/range)                                                                                                                                                                                     |
|                                                                                                                                                                     | `range` using `float`                                                                                                                                                 |                                                                                                              | [`float_range`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/range)                                                                                                                                                                                       |
|                                                                                                                                                                     | `range` using `long`                                                                                                                                                  |                                                                                                              | [`long_range`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/range)                                                                                                                                                                                        |
|                                                                                                                                                                     | `range` using `double`                                                                                                                                                |                                                                                                              | [`double_range`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/range)                                                                                                                                                                                      |
|                                                                                                                                                                     | `range` using `ipv4` or `ipv6` depending on IPv4 or IPv6                                                                                                              |                                                                                                              | [`ip_range`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/range)                                                                                                                                                                                          |
| [`Array`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Array.html#polars.datatypes.Array "polars.datatypes.Array") 2d                      | `matrix`                                                                                                                                                              | [`dynamic`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/dynamic?view=microsoft-fabric)   |                                                                                                                                                                                                                                                                                    |
| [`List`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.List.html#polars.datatypes.List "polars.datatypes.List") 1d                          | `multivalue` / `mv`<br>Passively handled in some cases.                                                                                                               | [`dynamic`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/dynamic?view=microsoft-fabric)   |                                                                                                                                                                                                                                                                                    |
| [`Field`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Field.html#polars.datatypes.Field "polars.datatypes.Field") key-value               | Doesn't really exist as nested data is passive and built into the system.                                                                                             | [`dynamic`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/dynamic?view=microsoft-fabric)   |                                                                                                                                                                                                                                                                                    |
| [`Struct`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Struct.html#polars.datatypes.Struct "polars.datatypes.Struct")                     | A set of fields                                                                                                                                                       | [`dynamic`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/dynamic?view=microsoft-fabric)   |                                                                                                                                                                                                                                                                                    |
| [`String`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.String.html#polars.datatypes.String "polars.datatypes.String")                     | `string`                                                                                                                                                              | [`string`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/string?view=microsoft-fabric)     |                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                     | Stored as a `string`, although constant_keyword could be optimized into an enum.                                                                                      |                                                                                                              | [`keyword, constant_keyword, wildcard`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/keyword)                                                                                                                                                             |
|                                                                                                                                                                     | Binary stored as a base64 `string`. Would have to be decoded into `binary` type via a function.                                                                       |                                                                                                              | [`binary`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/binary)                                                                                                                                                                                           |
| [`Categorical`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Categorical.html#polars.datatypes.Categorical "polars.datatypes.Categorical") |                                                                                                                                                                       |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`Enum`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Enum.html#polars.datatypes.Enum "polars.datatypes.Enum")                             | `enum`                                                                                                                                                                |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`Utf8`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Utf8.html#polars.datatypes.Utf8 "polars.datatypes.Utf8")                             | Folded into `string`                                                                                                                                                  |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`Binary`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Binary.html#polars.datatypes.Binary "polars.datatypes.Binary")                     | `binary`                                                                                                                                                              |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`Boolean`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Boolean.html#polars.datatypes.Boolean "polars.datatypes.Boolean")                 | `bool`                                                                                                                                                                | [`bool`](https://learn.microsoft.com/en-us/kusto/query/scalar-data-types/bool?view=microsoft-fabric)         |                                                                                                                                                                                                                                                                                    |
| [`Null`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Null.html#polars.datatypes.Null "polars.datatypes.Null")                             | `null`                                                                                                                                                                |                                                                                                              |                                                                                                                                                                                                                                                                                    |
| [`Object`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Object.html#polars.datatypes.Object "polars.datatypes.Object")                     | `object`                                                                                                                                                              |                                                                                                              | [`object`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/object), [`flattened`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/flattened), [`nested`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/nested) |
| [`Unknown`](https://docs.pola.rs/api/python/stable/reference/api/polars.datatypes.Unknown.html#polars.datatypes.Unknown "polars.datatypes.Unknown")                 | `unknown`<br>Failover if given something weird                                                                                                                        |                                                                                                              |                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                     | Resolved on ingestion                                                                                                                                                 |                                                                                                              | [`alias`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/field-alias)                                                                                                                                                                                       |
|                                                                                                                                                                     | Super meta for querying elastic with. I believe these are resolved when Elastic is queried, so Hql should never see it.                                               |                                                                                                              | [`join`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/parent-join), [`passthrough`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/passthrough)                                                                                    |
|                                                                                                                                                                     | `list` of `float`                                                                                                                                                     |                                                                                                              | [`point`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/point) [`geo_point`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-point)                                                                                              |
|                                                                                                                                                                     | `matrix` of `float`                                                                                                                                                   |                                                                                                              | [`shape`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/shape) [`geo_shape`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape)                                                                                              |

## Ranges
Most types can be ranged. Below an IP range is defined in Hql, then symbolized via a json object:
```
| extend ips = (192.168.0.0 .. 192.168.100.255)

{
	"ips": {
	    "start": "192.168.0.0",
	    "end": "192.168.100.255"
	}
}
```
Which is then translated into a struct in Polars, but treated differently when handled by Hql. Above a IPv4 address is shown, but it is cast to a `ip4` type, that is a Polars `UInt32`, then a comparison is done like:
```
pl.col("src_ip").is_between(
	pl.col("ips").col("start"),
	pl.col("ips").col("end")
)
# aka
pl.col("src_ip").is_between(3232235520, 3232261375)
```
You can then do comparisons in Hql like:
```
| extend ips = (192.168.0.0 .. 192.168.3.255)
| extend ips = 192.168.0.0/22
// preferred
| where src_ip in ips
// or, semantically identical
| where src_ip between ips
```
## Kusto-like Dynamic Values
In Kusto anything that doesn't fit a scalar value is given the type 'dynamic'. This includes json, nested objects, arrays, and lists. Since Hql is based on the principal of nested data, mimicking no-sql data, the dynamic type is absorbed into regular structures.
```
| extend kv = parse_json('{"a1":100, "a b c":"2015-01-01"}')
{
	"kv": {
		"a1": 100,
		"a b c": "2015-01-01"
	}
}
| project kv.['a b c']
{
	"a b c": "2015-01-01"
}

| extend list = parse_json('[100,101,102]')
{
	"list" [
		100,
		101,
		102
	]
}
| project list[1]
{
	"list": 101
}
```
When loaded in as a list, it will then be treated as a multi-value field. See below.
## Multi-values (mv)
Multi-values are a special way to treat list and objects in Hql. For example, you can have a field hold the contents of a list, giving it multiple values. Visually, and semantically, a single row in a field can have multiple values without the rest of the rows being affected. There are two types of multi-values, an object or a list. Since Hql treats objects differently than Kusto, you're able to treat about any field as a multi-value as long as it has children. Below are some examples
```
// Input
[
	{
		"User": {
			"name": "hashfastr",
			"first": "Sylvain",
			"last": "Jones"
		},
		"IP": "240.12.4.60"
	},
	{
		"User": {
			"name": kabdul,
			"first": [
				"Kareem",
				"Lew"
			],
			"last": [
				"Abdul-Jabbar",
				"Alcindor"
			]
		},
		"IP": "10.100.1.50"
	},
	{
		"User": {
			"name": "grapes",
			"first": "grapes",
			"last": null
		},
		"IP": [
			"192.168.125.33",
			"10.242.25.4",
			"172.16.55.8"
		]
	}
]

// Can be queried as such
| where IP in 10.0.0.0/8
| project username = User.name

[
	{"username": "hashfastr"},
	{"username": "sventek"},
	{"username": "grapes"}
]

// Or looking for names:
| where User.first == "Kareem"
| project firstname = User.first, lastname = User.last

[
	{
		"firstname": [
			"Kareem",
			"Lew"
		],
		"lastname": [
			"Abdul-Jabbar",
			"Alcindor"
		]
	}
]
```
Multi-value operators can then be used on these above.

Multi-value is also really good for summarize operators as well:
```
// input
[
	{
		"User": {
			"name": "grapes",
			"first": "grapes",
			"last": null
		},
		"IP": "192.168.125.33"
	},
		{
		"User": {
			"name": "grapes",
			"first": "grapes",
			"last": null
		},
		"IP": "10.242.25.4"
	},
		{
		"User": {
			"name": "grapes",
			"first": "grapes",
			"last": null
		},
		"IP": "172.16.55.8"
	}
]

| summarize make_list(IP) by User.name
// OR (preferred)
| summarize by User.name list IP

// Then this can be filtered on like any other multi-value field
[
	{
		"User": {
			"name": "grapes"
		}
	},
	"IP": [
		"192.168.125.33",
		"10.242.25.4",
		"172.16.55.8"
	]
]
```