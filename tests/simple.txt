syslog-*
| where Username == "hashfastr"
| project TimeGenerated, Username