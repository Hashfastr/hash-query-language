database('json').file('./notebooks/so-network-data.json')
| unnest _source on ['./notebooks/so-network-data.json']
| take 10 from ['./notebooks/so-network-data.json']
//| take 100 from ['./notebooks/big.json']
| count to _count