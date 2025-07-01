database('json').http('tf11-so-network.json')
| unnest _source
| project toip4(source.ip)
| where source.ip in (ip4subnet('192.168.0.0/16'), toip4("40.74.108.123"))
| summarize count() by source.ip
| sort by count_
