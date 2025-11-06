database('tf11-elastic').index('so-beats-*')
| extend EventCode = event.code
//| project EventCode
| where EventCode == 1
| take 1
