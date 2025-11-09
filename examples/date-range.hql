database('tf11-elastic').index('so-beats-*')
| where event.created between (datetime(2022-10-15T12:00:00.000Z) .. datetime(2022-10-25T12:00:00.000Z) )
| take 10
