database('json').file('./notebooks/so-network-data.json')
| unnest _source on ['./notebooks/so-network-data.json']
| project ['@version'], network.data.decoded
| extend log_version=tofloat(['@version'])
| take 10