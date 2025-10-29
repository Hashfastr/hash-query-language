let IOCs = datatable (executable: string)
[
  @'C:\Windows\System32\svchost.exe'
];
let Elastic = database('tf11-elastic').index('so-beats-*')
| project-rename executable = process.executable;
IOCs
| join Elastic on executable 
