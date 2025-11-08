/**
 * @title my detection
 * @author Unknown
 * @id 8bcfde90-6ab8-440b-a611-1493c2969e67
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
 * - 2025-11-08 Username: Init detection
 */
database('death-splunk').index('windows')
| take 10
| project res = scot4()
