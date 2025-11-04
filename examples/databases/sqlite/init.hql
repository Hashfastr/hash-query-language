database('nist-rds').index('METADATA')
| where md5 == 'AAB634FA7C0EEEE6EE64C138A5FDBC89'
//| where name contains 'Microsoft'
| take 1
