database('json').http('tf11-so-network.json')
| unnest _source
| project ['@timestamp'], toip4(source.ip), source.port, toip4(destination.ip), destination.port
| take 10