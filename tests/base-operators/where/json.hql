database('json').file('./notebooks/so-network-data.json')
| unnest _source on ['./notebooks/so-network-data.json']
| extend dest_ip = toip4(destination.ip)
| project dest_ip
| take 10