database("tf11-elastic").index("so-network-2022.*")
| where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z")
| where log.id.uid == "CAnltOiClThlO6ZFk"
| project log.id.uid
//| where client.ip_bytes == 1331
//| project client.ip_bytes
//| take 2