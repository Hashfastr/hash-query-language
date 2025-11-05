/**
 * @title my detection
 * @author Unknown
 * @id 192e5735-aa33-49ac-a75a-a75aaffea148
 * 
 * @status testing
 * @level medium
 * @schedule 0 * * * *
 * @description Parasaurolophus is a great dinosaur
 * 
 * @tags
 * - tag
 * 
 * @triage drink celsius
 * @falsepositives
 * - certainly
 * 
 * @authornotes 
 * @references
 * - https://hql.dev
 * 
 * @changelog
 * - 2025-11-05 Username: Init detection
 */
database('splunk').index('windows')
| where EventCode == 1
| where SHA1 == 'EB42621654E02FAF2DE940442B6DEB1A77864E5B'
| count
