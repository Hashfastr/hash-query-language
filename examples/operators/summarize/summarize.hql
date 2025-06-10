database('json').http('tf11-so-network.json')
| unnest _source
| extend ips = make_mv(toip4(source.ip), destination.ip)
| project source.ip, destination.ip, ips
| take 10
//| summarize count() by source.ip