database('splunk').index('windows')
| where EventCode == 1
| where SHA1 == "EB42621654E02FAF2DE940442B6DEB1A77864E5B"
| count
