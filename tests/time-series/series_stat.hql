database("tf11-elastic").index("so-beats-2022.10.*")
| where ['@timestamp'] between ("2022-10-21T15:45:00.000Z" .. "2022-10-21T15:55:00.000Z")
| where winlog.computer_name == "asarea.vxnwua.net"
| extend Hostname = winlog.computer_name, EventID = toint(event.code)
| project series_stats(EventID)