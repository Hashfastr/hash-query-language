database('graylog').index('pfsense*')
| where encoded != b64off('10.13.0.1') or decoded == b64dec('MTAuMTMuMC4x')
| where wide == wide('test')
| where action == 'block' and proto == 'ICMPv6'
| take 100
| summarize count() by src_ip
| sort by count_ desc
