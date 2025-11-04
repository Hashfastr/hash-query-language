let Meta = database('nist-rds').index('METADATA');
let Application = database('nist-rds').index('PACKAGE_OBJECT')
| join database('nist-rds').index('APPLICATION') on package_id
;
let Manu = database('nist-rds').index('MANUFACTURER_APPLICATION')
| join database('nist-rds').index('MANUFACTURER') on manufacturer_id
;
/*
Meta
| where md5 == 'AAB634FA7C0EEEE6EE64C138A5FDBC89'
| take 1
| join Application on object_id
| join Manu on application_id
*/
Meta
| where md5 == 'AAB634FA7C0EEEE6EE64C138A5FDBC89'
| join Application on object_id
