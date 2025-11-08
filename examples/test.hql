database('tf11-elastic').index('waterusage')
| where program == 'conmon'
| where message contains 'sventek'
//| summarize count() by program
//| sort by count_ desc
