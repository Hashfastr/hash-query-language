database('json').http('tf11-so-network.json')
| where winlog.computer_name == "asarea.vxnwua.net"
| project toint(event.code)
| take 10