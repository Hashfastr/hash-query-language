database("tf11-elastic").index("so-beats-2022.10.*")
| where ['@timestamp'] between ("2022-10-21T15:40:00.000Z" .. "2022-10-21T15:50:00.000Z")
# Should be 84232
| count