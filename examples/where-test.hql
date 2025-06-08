database("tf11-elastic").so-beats-2022.10.*
| where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z")
| where event.code in (10, 11, 13, 3)
| project ['@timestamp'], host.name, host.os.name, process.command_line
| take 10000