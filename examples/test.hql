/**
 * @title Update VM connections
 * @schedule * * * * *
 */
database('splunk').index('sysmon')
| where HostName == 'compromised'
| project source_ip, dest_ip
| project res = dfir_iris(kind=networkconn)
