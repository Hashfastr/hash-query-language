In this repo should exist a script to build wheels for this project.

Namely I need the titular package defined in @pyproject.toml and the polars package polars-runtime-32 as there exists no prebuilt wheel for Python 3.14t.
Currently if people want to install Hql they must build polars from scratch which is quite the lift.
Building polars requires a bunch of resources, specifically ram.
It crashes on my laptop, and crashes on my mac, let alone the compile time to even get to the crash.

Goals:
- Create a script to auto build both pyhql and polars in independent podman containers.
    - Scripts should be in @scripts
- Output wheels to @dist

Secondary goals:
- Create the ability to build for M series macs
- Include a script for pypi and github for publishing releases.
