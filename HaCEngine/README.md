# HaC Engine
HaC (Hql as Code) Engine is a method to perform Detection as Code efficiently using Hql DaC files.

It works by taking in DaC files and registering their execution into a running daemon.
These detections have Cron definitions in their metadata that are then used to trigger these detections on a given time.
When triggered a container is created to run the detection, actions are configured in the engine to apply to each DaC file.

## Dags
Using this method: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#the-dag-decorator
