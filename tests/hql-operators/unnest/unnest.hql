database('json').file('./notebooks/so-network-data.json')
| unnest _source on ['./notebooks/so-network-data.json']
| take 1