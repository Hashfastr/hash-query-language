database('json').http('tf11-so-network.json')
| unnest _source
| where source.ip in (ip4subnet(['192.168.0.0/16']))
| summarize source.ip=make_mv(source.ip), count() by destination.ip
| sort by count_