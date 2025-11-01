This is Hash query language, aka Hql.
A dialect of Kusto Query Language, it seeks to be a universal query language, or the path to one.
This is a passion project that I started in March this year, and is meant to provide a full featured query language to any database backend, and full interoperability between them.

The initial motive was to provide me, other home labbers, and those without buckets of money to achieve the same level of DEATH as those who can afford something greater.
This then grew once I realized the further implications to detection engineering and my field in general.

Hql operates by acting as a hybrid compiler.
First, knowing a backend database's type, compiles what features it's able into into its language.
The goal is to dump as many Hql instructions into the backend database but maintain semantic compatibility.
For all instructions it cannot compile into a database, it then executes a database engine to complete each operation.

- Lucene or QueryDSL
    - Graylog
    - Elastic
    - Opensearch
- SPL/Splunk
- Kusto
- SQLite

The database engine, built on polars, effectively allows for any key-value type data to be queried by Hql.

- json/ndjson
- csv
- parquet
- evtx

Additionally, joins between desparate database types and data types are now supported by using this engine, albeit expensive.
But the ability exists now, and can enable many in having a lookup spreadsheet, sqlite, database, etc.

Another use here is if you're performing an engagement and they can only provide logs in CSV, or syslog, or a SIEM you don't have detections or a pipeline built for.
Uploading files to Splunk or ADX is alright, and works in certain sizes, but what if you have a lot of data, or want to heavily filter that data before it gets ingested?
Hql has a planned operator `push` that allows a query to push data to another database.
Use Hql to regex extract a multi-terabyte set of F5 logs, filter only for 2 hosts, then ingest into ADX.
Then deploy detections you've already written.

This then grows to DEATH.
Sigma is lacking fairly strongly in the features department, not able to outgrow Lucene limitations, which effectively represent the bare minimum.
This is fine, fairly readable, and programmatically easy to create if needed, but it can be so much more.
Hql detection as code, aka HaC, is the built in detection as code feature in Hql.
It enables truely carrying the detection with the code, not storing or maintaining them in separate locations.
This is done by using a deoxygen style comment above the query providing documentation context to the query.
Now you can edit and run the detection in the same place, removing the need to update detection, copy/paste the query, then update the documentation, then push.

Sigma isn't gone though, it's direct integrated and extended by Hql.
Hql can run sigma detections directly and bases its generic log specification on Sigma.
Hql then extends sigma by adding two fields to define a schedule to a Sigma query, and any post query operations.
If you want to move just to Hql and extend the detection, Hql is able to fully deparse Sigma into native Hql.

Many current DaC solutions, or implementations, rely on pipelines such as those with Sigma.
This removes that with the ability for built in git integration, and for Hql to run as its own detection server.
This decouples the restrictions of a SIEM such as Sentinel, or Splunk, to require you to use their detection scheduler.
One of my personal gripes is that Sentinel does not allow you to delete detections, requires arm template deployment, and the time specification for detections are vague, redeployment means possibly completely resetting the timer.
While fine for single-siem shops, people are acruing multiple desparate sources such as MDE, Crowdstrike, AWS, Azure, etc, which makes central management difficult.
This gives people the ability to manage detections their way, without restrictions.

Sending alerts can vary in how for each platform, but Hql looks to provide sending in a very custom manner.
Send emails, perform REST requests, and possibly more just by calling a function in the language.
This allows for something more interesting than creating a scot alertgroup or jira ticket.
When managing you can make a detection to gather the IPs talking to a computer in the last 5 minutes, every minute, and push it to a graph in DFIR IRIS.
Similarly, update host lists automatically with hosts that match IOC behavior.

Futher implications are that this allows for those restricted to a SIEM due to feature set have the ability to move to something else.
Splunk has gotten rediculously expensive, and will just keep going up as they have an effective monopoly.
So why not store certain logs in postgres, datalake, or elastic and still maintain that feature set?
Granted performance will be hindered, but it's possible.

Running Hql is decently easy, I didn't want to create something that required Kubernetes, Java, bleeding edge, so Hql requires at minimum Python 3.9.
This should work on my laptop without a PhD in figuring out how to run your stupid container.
I don't care if it'll scale I need to just run in the basecase!
However to run the HaC engine, and enable parallel processing, Python 3.14t, or 3.13t is needed.
It's hit a some of the mainstream distros, but people use RedHat, so I've provided a docker/podman container.
Using a free threaded build also requires compilation of polars on your host system, so you need rust set up.
Otherwise you can pip install it as a module and even use it as a library.

For this workshop I've hooked Hql up to a SIEM interface that interacts with the HaC engine over a REST API.
The possibility for hooking up a front end to a running HaC server allows for some cool possibilies.
Using Hql direct as a SIEM, and providing things that other languages like Splunk don't provide, such as field completion and type hinting.
These don't exist yet, but could in the future by caching schema from existing indexes and referring to them when using one.
A HaC front end would also allow for direct running, editing, and saving of detections.
Realistically, this could also be a VSCode plugin.
