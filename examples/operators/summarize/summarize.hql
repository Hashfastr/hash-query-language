database('json').http('tf11-so-network.json')
| unnest _source
| extend ips = make_mv(source.ip, destination.ip)
| project ['@timestamp'], source.ip, destination.ip, ips
| project-away ['@timestamp'], source.ip, destination.ip
| mv-expand ips to ip4
//| summarize count() by ips
| take 10