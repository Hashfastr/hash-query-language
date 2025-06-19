database('json').http('tf11-so-network.json')
| unnest _source
| project ['@timestamp'], src_ip=toip4(source.ip), src_port=source.port, dest_ip=toip4(destination.ip), dest_port=destination.port
| summarize count() by src_ip