database("tf11-elastic").so-beats-2022.10.*
| where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z")
| where event.code == 1
| where host.name == "asarea.vxnwua.net"