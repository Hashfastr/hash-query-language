database('json').file('./notebooks/big.json', './notebooks/so-network-data.json')
| where winlog.computer_name == "asarea.vxnwua.net"
| take 1
| project toint(event.code)