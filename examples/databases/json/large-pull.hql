// The source for this one is 125MB, so be cautious
database('json').http('tf11-so-beats-large.json')
| where winlog.computer_name == "asarea.vxnwua.net"
| project toint(event.code)
| take 10