database('json').http('tf11-so-network.json')
| unnest _source
| extend ips = make_mv(source.ip, destination.ip)
| mv-expand ips to ip4
| summarize count() by ips
| sort by count_