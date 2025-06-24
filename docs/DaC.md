# DaC Plan

Example using the sigma here: [Persistence Via Cron Files](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_persistence_cron_files.yml)

```
/**
 * @title  Persistence Via Cron Files
 * @author Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
 * @id     6c4e2f43-d94d-4ead-b64d-97e53fa2bd05
 * 
 * @status test
 * @level medium
 * @description
 * Detects creation of cron file or files in Cron directories which could
 * indicates potential persistence.
 * 
 * @tags
 * - attack.persistence
 * - attack.t1053.003
 * 
 * @triage
 * Investigate the crontab/cronfile created and what scripts/programs it runs
 * and as what user.
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
let DB = database('linux');
let LFE = DB.macro('file_events');
let Filename = LFE.field('TargetFilename');
let CronPaths = make_mv(
    '/etc/cron.d/',
    '/etc/cron.daily/',
    '/etc/cron.hourly/',
    '/etc/cron.monthly/',
    '/etc/cron.weekly/',
    '/var/spool/cron/crontabs/'
);
let CronFiles = make_mv(
    '/etc/cron.allow',
    '/etc/cron.deny',
    '/etc/crontab'
);
LFE
| where Filename startswith CronPaths or Filename contains CronFiles
```

The above is decently larger than the sigma query, 54 lines vs 33.
That's mostly due to added content such as the authornotes and triage sections.
Also the query is has portions split out over multiple lines for readability.
Should I remove these, and my change log entry, we get 33 lines ironically.
Although these are necessary for readability, usability, etc.

## Breaking down the DaC Example
We do a lot of let calls here, mostly for config management and readability.
You could collapse it down to something like this:

```
let CronPaths = make_mv(
    '/etc/cron.d/',
    '/etc/cron.daily/',
    '/etc/cron.hourly/',
    '/etc/cron.monthly/',
    '/etc/cron.weekly/',
    '/var/spool/cron/crontabs/'
);
let CronFiles = make_mv(
    '/etc/cron.allow',
    '/etc/cron.deny',
    '/etc/crontab'
);
database('linux').macro('file_events')
| where Filename startswith CronPaths or Filename contains CronFiles
```

The above assumes a lot and strips away the ability to be easily shared.
- Assume we know the fieldname always, across elastic/splunk/kusto.
- Assumes we know the fields we'd like to project to look nicer.

## Breaking past the sigma barrier
We can add a bunch of optimizations to the query to help the thrunter.
For example we can add a project to remove unnecessary fields.

```
LFE
| where Filename startswith CronPaths or Filename contains CronFiles
| project LFE.macro('linux_file_fields'), Filename
```

Here we can use splunk like macros predefined for us that can be defined on a per-deployment basis.
This is how it might look like with that macro expanded:

```
LFE
| where Filename startswith CronPaths or Filename contains CronFiles
| project ['@timestamp'], hostname, processname, user, pid, Filename
```

Which looks a hell of a lot better in a table, in an email, than just every field dumped into the same destination.

We could even add something more, what about summarizing info to break down data?
This doesn't really apply to this detection as something like this might not fire too often.

```
let User = LFE.field('user');
let Hostname = LFE.field('hostname');
LFE
| where Filename startswith CronPaths or Filename contains CronFiles
| project LFE.macro('linux_file_fields'), Filename
| summarize take_any(*) by LFE.field('user'), LFE.field('hostname'), Filename
```

Or maybe drop the summarization and do some info lookup on hashes:

```
LFE
| where Filename startswith CronPaths or Filename contains CronFiles
| extend VirusTotalReport = lookup_vt(LFE.field('parent_hash'))
| project LFE.macro('linux_file_fields'), Filename, VirusTotalReport
```

Let's just keep adding stuff.
Let's hunt on the parent hash in our other file logs.

```
let DB = database('linux');
let LFE = DB.macro('file_events');
let ParentHash = LFE.field('parent_hash');
// Cron IOCs would go here, omitting for simplicity
LFE
| where Filename startswith CronPaths or Filename contains CronFiles
| extend VirusTotalReport = lookup_vt(ParentHash)
| project LFE.macro('linux_file_fields'), Filename, ParentHash, VirusTotalReport
| join kind=leftouter (LFE | project LFE.macro('linux_file_fields')) on $left.ParentHash == $right.ParentHash and $left.VirusTotalReport.malware == True
```

This now looks for processes that have created these Cron files, then looks them
up in VT and if those VT reports say it's malware, then join that processes other
events onto us, adding them to the report.