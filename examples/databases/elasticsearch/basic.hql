database('ES').index('so-beats-*')
| where winlog.computer_name == "asarea.vxnwua.net"
//| where uptime > 10
//| project toint(event.code)
| take 10
| project Hostname=winlog.computer_name, IPs=host.ip
//| project Hostname, IPs
//| summarize count() by winlog.computer_name
