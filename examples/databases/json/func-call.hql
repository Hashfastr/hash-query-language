database('json').file('./notebooks/big.json', './notebooks/so-network-data.json')
| where winlog.computer_name == "asarea.vxnwua.net"
| project toint(event.code)
| take 10