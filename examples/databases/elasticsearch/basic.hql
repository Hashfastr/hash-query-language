database('ES').index('so-beats')
| where winlog.computer_name == "asarea.vxnwua.net"
| project toint(event.code)
| take 10
