database("tf11-elastic").['so-beats-2022.10.*']
| where isfuzzy = True event.code == 1