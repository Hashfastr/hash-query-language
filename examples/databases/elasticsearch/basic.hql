database('ES').index('*')
| where winlog.computer_name == "asarea.vxnwua.net"
//| where uptime > 10
//| project toint(event.code)
| take 10
| summarize count() by winlog.computer_name
