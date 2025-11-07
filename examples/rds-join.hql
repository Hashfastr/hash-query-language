let Meta = database('nist-rds').index('METADATA');
let Application = database('nist-rds').index('PACKAGE_OBJECT')
| join database('nist-rds').index('APPLICATION') on package_id
;
let Manu = database('nist-rds').index('MANUFACTURER_APPLICATION')
| join database('nist-rds').index('MANUFACTURER') on manufacturer_id
;
let RDS = Meta
| join Application on object_id
;
database('death-splunk').index('windows')
| where EventCode == 1
| extend sha256 = tolower(SHA256)
| take 10
| join RDS on sha256
