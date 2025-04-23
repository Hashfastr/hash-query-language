# Manifesto
Hash query language is essentially a re-implementation of [Kusto Query Language](https://github.com/microsoft/Kusto-Query-Language), Microsoft's answer to `SPL`.
This language however is exclusive to Azure solutions such as Azure Data Explorer, Log Analytics Workspaces and by extension Sentinel.

The idea here is to create a query language that can be used on-top of an existing Elasticsearch instance to make complex queries.
For example, in my home lab I use Graylog.
This provides nothing more than just basic filters and frankly sucks, but it was easy to set up.

For instance, I have a security incident where a user was compromised by a remote IP, let's say `240.1.33.7`.
How can I in a single query find all users who logged in from a common IP that this other user logged in as and make it a succinct summary?
In graylog or other elastic based SIEMs this does not exist, with the exception of `ES|QL` which I have very limited experience with.

Graylog would look like:
```
# Note down IP addresses here
filebeat_event_source_product:syslog AND program:sshd AND user:hashfastr AND status:Accepted

# limited example to 3 IPs, but you do need to find and enter them manually
filebeat_event_source_product:syslog AND program:sshd AND (IP:240.1.33.7 OR IP:240.6.23.8 OR IP:240.23.41.54) AND status:Accepted

# Note down users
# Create your own report
```

With the above example, this would be impossible to create an alert from it as it's multistage and requires manual intervention.
Now let's see how it might be done in Hql.

```
let AttackerIPs = syslog-*
| where program == "sshd" and user == "hashfastr" and status == "Accepted"
| project IP;
syslog-*
| where program == "sshd" and status == "Accepted"
| join kind=inner (AttackerIPs) on IP
| project timestamp, user, IP, authtype
```

Here it's extremely simple to thrunt from behavior relating to that nasty user 'hashfastr' and other behavior in logs.
In KQL or LAW like stuff you have tables instead of indexes, although they are similar in function.
Here instead of having a table like `SigninLogs` I'm going for something more flexible and native to Elasticsearch, index patterns.

Another thing this improves on, and I'm unsure how things like LAW handle this, but in Splunk queries are processed in steps.
That is `syslog-* | where ... | join ... | project ...` requires each step to full execute before the next.
It would be nice to stream the data, that is process other parts of the pipeline while the previous steps are being processed.

Anyways that's the idea.
It's gonna be written in python for right now since JSON is dead stupid using python.
But python doesn't have real concurrency, and is comparatively slow, so maybe a mixed language situation?