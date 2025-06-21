database('json').http('tf11-so-network.json')
| unnest _source
| extend ips = make_mv(source.ip, destination.ip)
//| project source.ip, destination.ip, ips
| summarize count() by source.ip, destination.ip
| take 10