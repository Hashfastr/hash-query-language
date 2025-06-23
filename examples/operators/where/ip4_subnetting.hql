database('json').http('tf11-so-network.json')
| unnest _source
| project toip4(source.ip)
//| project source
| where source.ip in (ip4subnet(['192.168.0.0/16']))
| summarize count() by source.ip
//| sort by count_
| take 10