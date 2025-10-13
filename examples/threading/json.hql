/**
 * @title  Persistence Via Cron Files
 * @author Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
 * @id     6c4e2f43-d94d-4ead-b64d-97e53fa2bd05
 * 
 * @status test
 * @level medium
 * @schedule * * * * *
 * @description
 * Detects creation of cron file or files in Cron directories which could
 * indicates potential persistence.
 *
 * Does a VT look up on processes that do, and joins their other activity
 * throughout the network if VT gets a positive hit for maliciousness.
 * 
 * @tags
 * - attack.persistence
 * - attack.t1053.003
 * 
 * @triage
 * Investigate the crontab/cronfile created and what scripts/programs it runs
 * and as what user.
 * If VT Hits, the log will be flagged and other activity will be included as
 * well, which will help with pivoting.
 * 
 * @falsepositives
 * - Any legitimate cron file
 * 
 * @authornotes
 * I couldn't really know what the second update was because of the fog of git.
 * You'd also put something here that a incident responder would like when
 * receiving an alert from this.
 * 
 * @references
 * - https://github.com/microsoft/MSTIC-Sysmon/blob/f1477c0512b0747c1455283069c21faec758e29d/linux/configs/attack-based/persistence/T1053.003_Cron_Activity.xml
 * 
 * @changelog
 * - 2021-10-15 Cyb3rWard0g: Initial commit
 * - 2022-12-31 Cyb3rWardog: Some sort of update
 * - 2025-06-23 Hashfastr:   Hql conversion
 */
union database('json').macro('all'), database('json').macro('all'), database('json').macro('all'), database('json').macro('all')
| project ['@timestamp'], src_ip=toip4(source.ip), src_port=source.port, dest_ip=toip4(destination.ip), dest_port=destination.port
| union test as test
| take 10
