# Functions
## Planned not implemented

Functions are a way to integrate other data sources along with additional computing in a query.
A standard Kusto function found in Azure is as follows:

```
SigninLogs
| extend Location = geoip_fl(IPAddress)
```

Here we add a new column to our dataset by taking the value of the `IPAddress` column and running it through the `geoip_fl` function on a per-row basis.
[These functions can get kinda crazy](https://learn.microsoft.com/en-us/kusto/query/functions/user-defined-functions?view=microsoft-fabric), but still only basic arithmetic and logic (I could be wrong here).
For a user to extend this functionality to do literally anything, I'm not sure it currently exists in Kusto as Microsoft presents it.

To solve this Hql will support user-defined functions in whatever language as long as it follows a standard API to talk to each container.
For example, an extend container should be able to communicate to Golang function as well as a Rust function.
How? I don't know yet, one step at a time.

An example usage might be using Polarity, Shodan, Virustotal, etc in a query:

```
// psuedo code if not obvious

sysmon
| extend VirusTotal = lookup_vt(SHA256)

// or

SigninLogs
| extend Shodan = shodan(IPAddress)

// or

vpnlogs
| extend Polarity = polarity(IPAddress)
```

And the function would then be a modular piece of code available at run time that is able to take a value and query it back to an API.
Another thing could be AI, internal tools, or even data analytics libraries.

How? Still figuring it out. But it'd be cool, right?