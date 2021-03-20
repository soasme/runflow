Concepts
========

Worker
------

A worker is Jetflow runtime on a single machine. A Jetflow service is formed by a cluster of workers.

Executor
--------

An executor is the job runner.  For example, a python Task class can run in a Thread Executor or Process Executor, a docker container can run in an ECS Executor.

GUI/API
-------

Jetflow exposes its main functionality via HTTP GUI/API.

To operate Jetflow jobs, you can either use Jetflow GUI or through API.
Optionally, if you are an IaaS fan, there is a Terraform provider you can use, which uses Jetflow HTTP API.

Metadata Database
-----------------

Jetflow metadata is stored in a SQL database. Currently, it supports SQLite3, MySQL, and PostgreSQL.
