/**
 * @title my detection
 * @author Unknown
 * @id 9ffadf02-1656-4e5e-8b9b-f655594d075e
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
database('tf11-elastic').index('so-beats-*')
| where winlog.computer_name matches regex 'as.rea.*'
| project Hostname=winlog.computer_name, IPs=host.ip
| summarize count() by Hostname
