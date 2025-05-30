database("tf11-elastic").so-beats-2022.10.*
| where ['@timestamp'] between ("2022-10-21T00:00:00.000Z" .. "2022-10-22T00:00:00.000Z")
| where event.code == 1
| project ['@timestamp'], host.name, host.os.name, process.command_line