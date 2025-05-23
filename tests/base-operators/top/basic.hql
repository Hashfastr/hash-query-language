database("tf11-elastic").index("so-network-2022.*")
| where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z")
| project client.ip_bytes
//| take 2