database("tf11-elastic", "SCROLL_MAX=1").index("so-beats-2022.10.*")
| where _id == "CZI8-4MBqn-zbgNiq9cL" or _id == "AZI8-4MBqn-zbgNiq9cL"