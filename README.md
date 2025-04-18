# Hash Query Language (HQL)
Hash query language is essentially a re-implementation of [Kusto Query Language](https://github.com/microsoft/Kusto-Query-Language), Microsoft's answer to `SPL`. This language however is exclusive to Azure solutions such as Azure Data Explorer, Log Analytics Workspaces and by extension Sentinel.

The idea here is to create a query language that can be used on-top of an existing Elasticsearch instance to make complex queries. For example, in my home lab I use Graylog. This provides nothing more than just basic filters and frankly sucks, but it was easy to set up.

For instance, I have a security incident where a user was compromised by a remote IP, let's say `240.1.33.7`. How can I in a single query find all users who logged in from a common IP that this other user logged in as and make it a succinct summary? In graylog or other elastic based SIEMs this does not exist, with the exception of `ES|QL` which I have very limited experience with.

Graylog would look like:
```
# Note down IP addresses here
filebeat_event_source_product:syslog AND program:sshd AND user:hashfastr AND status:Accepted

# limited example to 3 IPs, but you do need to find and enter them manually
filebeat_event_source_product:syslog AND program:sshd AND (IP:240.1.33.7 OR IP:240.6.23.8 OR IP:240.23.41.54) AND status:Accepted

# Note down users
# Create your own report
```

With the above example, this would be impossible to create an alert from it as it's multistage and requires manual intervention. Now let's see how it might be done in HQL.

```
let AttackerIPs = syslog-*
| where program == "sshd" and user == "hashfastr" and status == "Accepted"
| project IP;
syslog-*
| where program == "sshd" and status == "Accepted"
| join kind=inner (AttackerIPs) on IP
| project timestamp, user, IP, authtype
```

Here it's extremely simple to thrunt from behavior relating to that nasty user 'hashfastr' and other behavior in logs. In KQL or LAW like stuff you have tables instead of indexes, although they are similar in function. Here instead of having a table like `SigninLogs` I'm going for something more flexible and native to Elasticsearch, index patterns.

Another thing this improves on, and I'm unsure how things like LAW handle this, but in Splunk queries are processed in steps. That is `syslog-* | where ... | join ... | project ...` requires each step to full execute before the next. It would be nice to stream the data, that is process other parts of the pipeline while the previous steps are being processed.

Anyways that's the idea. It's gonna be written in python for right now since JSON is dead stupid using python. But python doesn't have real concurrency, and is comparatively slow, so maybe a C family rewrite? golang? rust :vomit:?

## Setup
```
# you need java
source ./setup-antlr4.sh

# Generates the python files needed
antlr4 -Dlanguage=Python3 -visitor ./grammar/Hql.g4
```

## Running
Still a bit a manual process to run, doesn't return data anywhere.

```
python3 Hql.py -f ./tests/tf11-simple.txt
```

This will compile out a compose file and container config files for use.
Each query set has a guid, each container has a guid.

```
./out
     /b8d1fad3
              /compose.yml
              /index-c4fb3561.json
```

Where `b8d1fad3` is the query guid, and `c4fb3561` is the container guid.
The compose then creates services named after the type of container and its guid.
The network created is also named after the query's guid.

Then running will execute the query:

```
cd ./out/b8d1fad3
podman compose up
```

## Debug
### Generating graphs using grun
Where previously we compiled antlr to python, we need to compile it to java for grun.
Make sure you already setup antlr4 using the setup script as seen in the previous section.

```
# this generates *a lot* of java and class files
cd grammar
antlr4 -Dlanguage=Java -visitor Hql.g4
javac -cp ../antlr4/antlr-*-complete.jar Hql*.java

# runs until you kill / Ctrl-C / close the window
grun Hql top ../tests/simple.txt -gui

# Clean up via
rm *.java *.class
```