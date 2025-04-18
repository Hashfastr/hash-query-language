Q: Why use containers for each operation and not just compile directly to a python program for each individual query?

A:
The goal I want in the end is being able to utilize set theory, and using multiple independent containers allows for that. This is mainly for doing a set of detections, or much more complex queries.

Imagine 10 detections that use the same source data that covers a large area of time. This could be taxing on a system to do this ten times individually. Or, the group of detections are compiled together and a singular index container is placed at the top, and once the different queries diverge then they get their own containers.

Another reason is that this can allow for us to stream data as it comes out. Process other parts of the pipeline while previous parts are being processed.

**Reduce repeat processing, increase parallelism, and allow streaming.**

---

