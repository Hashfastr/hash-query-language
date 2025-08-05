// More of a parser test here
// Logically this is garbage
// Shouldn't return anything
database('json').http('tf11-so-network.json')
| unnest _source
| where source.ip > 10 and source.ip < 10 or source.ip == "test" or source.ip >= 10 and source.ip <= 10 and source.ip != 10
| project source.ip
