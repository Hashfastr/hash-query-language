database('json').file('./notebooks/so-network-data.json')
| unnest _source on ['./notebooks/so-network-data.json']
| extend dest_ip = toip4(destination.ip), port_stats = series_stats(destination.port)
| project dest_ip, port_stats
| take 10