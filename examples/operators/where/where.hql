database('json').http('tf11-so-network.json')
| unnest _source
| extend ip = make_mv(source.ip, destination.ip)
| mv-expand ip to ip4
| where ip in (ip4subnet(['192.168.0.0/16']))
| summarize count() by ip
| sort by count_