// shows off some multithreading and multi-tables
union database('json').macro('all'), database('json').macro('all')
| project ['@timestamp'], src_ip=toip4(source.ip), src_port=source.port, dest_ip=toip4(destination.ip), dest_port=destination.port
| where isnotempty(src_ip)
| summarize count() by src_ip
| sort by count_ desc
| take 10
