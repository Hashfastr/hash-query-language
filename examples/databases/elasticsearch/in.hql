database('tf11-elastic').index('so-beats-*')
//| where winlog.computer_name != 'asarea.vxnwua.net'
| where winlog.computer_name in ("asarea.vxnwua.net", "AD.vxnwua.net", "rpatel.vxnwua.net")
| where event.code == "1"
//| project toint(event.code)
| take 10
| project Hostname=winlog.computer_name, IPs=host.ip, EventCode = event.code
//| project Hostname, IPs
//| summarize count() by Hostname, 
