---
sidebar: auto
---

# Integrate With APScheduler

Runflow does not come with a default scheduler, but it's easy to be
overcome with some existing scheduling solutions, such as
[APScheduler](https://apscheduler.readthedocs.io/).

## Project Layout

Assume you have a project layout like below:

```bash
your_package/
    sched.py
    flows/
        flow_1.hcl
        flow_2.hcl
        ...
```

The file content of `sched.py` is like any other APScheduler program:

* Set `func` to `'runflow:runflow'`.
* You can provide either `module`, `path`, or `source` in `kwargs` to specify which flow spec to use .
* You can provide `vars` in `kwargs` to specify the variables for the flow spec.

```python
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

sched = AsyncIOScheduler()

def main():
    sched.add_job(
        func='runflow:runflow',
        kwargs={
            'module': 'your_package.flows.flow_1:flow',
            'vars': {}
        },
        trigger='interval',
        seconds=10,
    )

    sched.start()
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    main()
```

Run it:

```
$ python3 -m your_package.sched
```
