database("tf11-elastic").index("so-beats-2022.10.*")
| where winlog.computer_name == "asarea.vxnwua.net"
| extend Hostname = winlog.computer_name, EventID = toint(event.code)
| project ['@timestamp'], Hostname, EventID
| project series_stats(EventID)