database('graylog').index('pfsense*')
| where action == 'block' and proto == 'ICMPv6' and test == toip4('10.13.0.1')
| take 100
| summarize count() by src_ip
| sort by count_ desc
