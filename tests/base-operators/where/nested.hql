database("tf11-elastic").index("so-beats-2022.10.*")
| where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z") and (event.code == 11 or host.name == "asarea.vxnwua.net")
| where process.pid == 1456
// Nuke protection, results should be exactly 117
| take 200
| count