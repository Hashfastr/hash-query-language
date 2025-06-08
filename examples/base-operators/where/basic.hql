database("tf11-elastic").['so-beats-2022.10.*']
| where process.pid == 7716
// Anti-nuke protection, should only be 960
| take 1000
| count