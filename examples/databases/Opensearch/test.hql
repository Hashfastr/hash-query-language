database('graylog').index('pfsense*')
| where test == toip4('10.13.0.1') and action == 'block' and proto == 'ICMPv6'
| take 100
| summarize count() by src_ip
| sort by count_ desc
