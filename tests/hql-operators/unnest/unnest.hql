database('json').file('./notebooks/so-network-data.json')
| unnest _source on ['./notebooks/so-network-data.json']
//| project event.severity
| take 10