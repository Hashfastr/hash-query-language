# HaC Engine
HaC (Hql as Code) Engine is a method to perform Detection as Code efficiently using Hql DaC files.

It works by taking in DaC files and registering their execution into a running daemon.
These detections have Cron definitions in their metadata that are then used to trigger these detections on a given time.
When triggered a container is created to run the detection, actions are configured in the engine to apply to each DaC file.

## Dags
Using this method: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#the-dag-decorator

I use podman for my containers, this was tested on RHEL 9.6 (for now...).
The compose is configured to use SELinux, be not afraid.
If you want to use docker then just replace `podman` with `docker` in commands.
You're smart, figure it out.

Starting things:
```
# Set the UID for whatever user you're using with podman
echo -e "AIRFLOW_UID=$(id -u)" > .env

# Compose up
podman compose up -d
```

Then the interface is hosted at http://localhost:8080, which you can change or proxy to of course.
Default creds are `airflow`/`airflow` and you should change them.

## Troubleshooting
### Remove Airflow Example Dags
If the example dags load, you can remove them by specifying `load_examples = False` in `config/airflow.cfg`.
Normally this is an env variable in the compose, but doesn't seem to actually work.
It is likely you'll have to do this.
Or you could not, you'll just have a bunch of garbage in your airflow.

You then need to remove them from the DB via:

```
podamn exec hacengine_airflow-apiserver_1 /bin/bash
airflow db reset

# Then outside of the container
podman compose down
podman compose up -d
```


