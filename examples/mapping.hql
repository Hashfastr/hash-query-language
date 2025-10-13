database('tf11-elastic').index('so-beats-*')
| project Hostname=winlog.computer_name, IPs=host.ip
| where Hostname == 'asarea' and IPs == '192.168.1.1'
