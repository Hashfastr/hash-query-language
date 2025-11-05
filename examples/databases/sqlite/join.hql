let Meta = database('nist-rds').index('METADATA');
let Application = database('nist-rds').index('PACKAGE_OBJECT')
| join database('nist-rds').index('APPLICATION') on package_id
;
let Manu = database('nist-rds').index('MANUFACTURER_APPLICATION')
| join database('nist-rds').index('MANUFACTURER') on manufacturer_id
;
Meta
//| where md5 == 'aab634fa7c0eeee6ee64c138a5fdbc89'
//| join Application on object_id
| where file_name == "cmd.exe"
| take 10
//| project md5
