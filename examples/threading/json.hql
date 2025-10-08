database('json').macro('all')
| project ['@timestamp'], src_ip=toip4(source.ip), src_port=source.port, dest_ip=toip4(destination.ip), dest_port=destination.port
| extend _time = ['@timestamp']
| take 10
//| summarize count() by src_ip
