database('graylog').index('pfsense*')
| where action == 'block' and proto == 'ICMPv6'
| take 100
| summarize count() by src_ip
| sort by count_ desc
