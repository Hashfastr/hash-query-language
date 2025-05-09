database("tf11-elastic").index("so-beats-2022.10.*")
| where winlog.computer_name == "asarea.vxnwua.net"
| take 10
| extend Hostname = winlog.computer_name, EventID = event.code
| project ['@timestamp'], Hostname, EventID