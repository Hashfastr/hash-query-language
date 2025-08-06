database('ES').index('so-beats-*')
| where winlog.computer_name == "asarea.vxnwua.net"
//| where uptime > 10
//| project toint(event.code)
| take 10
| project winlog.computer_name, host.ip
| extend Hostname = winlog.computer_name, IPs = host.ip
//| summarize count() by winlog.computer_name
