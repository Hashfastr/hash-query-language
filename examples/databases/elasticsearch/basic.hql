database('tf11-elastic').index('so-beats-*')
| where winlog.computer_name matches regex "as.rea.*"
| project Hostname=winlog.computer_name, IPs=host.ip
| summarize count() by Hostname
