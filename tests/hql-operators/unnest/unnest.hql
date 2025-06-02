database('json').file('./notebooks/so-network-data.json')
| unnest _source on ['./notebooks/so-network-data.json']
| project ['@version'], network.data.decoded
| extend log_version=toint(['@version'])
| take 10