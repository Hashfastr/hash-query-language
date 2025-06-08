database("tf11-elastic").index("so-beats-2022.10.*")
| where winlog.computer_name == "asarea.vxnwua.net"
| extend client_ip = metadata.ip_address, hostname = winlog.computer_name
| join type=inner (
    database("tf11-elastic").index("so-network-2022.*")
    | extend client_ip = server.ip, client_port = client.port, dest_ip = destination.ip, dest_port = destination.port
    | project client_ip, client_port, dest_ip, dest_port
  ) on src_ip
| project hostname, client_ip, client_port, dest_ip, dest_port