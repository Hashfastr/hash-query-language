let RDS = database('nist-rds').index('METADATA');
let Splunk = database('splunk').index('windows')
| where EventCode == 1
;
Splunk
| project-rename md5=MD5
| take 100
| join RDS on md5
