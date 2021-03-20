.. Jetflow Internal::

Jetflow Internal
================

Jetflow Worker
--------------

A Jetflow worker is a Python program. It has an asyncio main loop running.
The event loop runs an ASGI app using uvicorn+starlette, and a scheduler app
using APScheduler. 

Let's say, we send a POST request to http://localhost:8964/scheduler/jobs. Uvicorn handles
the request and sends request information to Starlette ASGI interface.
The API resource adds the job to metadata database and sends back a JSON response
via ASGI interface through to Uvicorn.

APScheduler app inside a Jetflow worker acquires some jobs from metadata database
and triggers them locally. Jobs can run locally or remotely depending on how
the job is defined.
