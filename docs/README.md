# Runflow

Welcome to Runflow's documentation.

[![Stars](https://img.shields.io/github/stars/soasme/runflow?style=social)](https://github.com/soasme/runflow)
[![Pypi](https://img.shields.io/pypi/v/runflow?style=social)](https://pypi.org/project/runflow/)
[![License](https://img.shields.io/github/license/soasme/runflow?style=social)](https://github.com/soasme/runflow/blob/main/LICENSE)

<div style="background-image: url('/logo.svg'); background-position: 0 -185px; background-repeat: no-repeat; height: 125px;"></div>

## Getting Started

* Get started with [Installation](installation.md).
* Get an overview with the [Quick Start](quickstart.md).
* Get familiar with Runflow [Concepts](concepts.md).

## Hello World 👋

<<< @/examples/hello.hcl

## References

Flow:

* References: [Runflow Specification](flow-spec.md).
* References: [Built-In Functions](builtin-functions.md).

Tasks:

* References: [Bash Run](tasks/bash-run.md) Task.
* References: [Docker Run](tasks/docker-run.md) Task.
* References: [Flow Run](tasks/flow-run.md) Task.
* References: [File Write](tasks/file-write.md) Task. Runflow supports these file systems: GitHub, FTP, SFTP, Arrow HDFS, HTTP, Zip, local Git repo, SMB, etc.
* References: [File Read](tasks/file-read.md) Task. Runflow supports these file systems: GitHub, FTP, SFTP, Arrow HDFS, HTTP, Zip, local Git repo, SMB, etc.
* References: [Hcl2 Template](tasks/hcl2-template.md) Task.
* References: [Http Request](tasks/http-request.md) Task.
* References: [Sql Exec](tasks/sql-exec.md) Task. Runflow supports these databases: SQLite3, MySQL, PostgreSQL, MSSQL, Oracle, etc.
* References: [Sql Row](tasks/sql-row.md) Task. Runflow supports these databases: SQLite3, MySQL, PostgreSQL, MSSQL, Oracle, etc.


## Advanced Usage

* Advanced Usage: Use [Python API](python-api.md).
* Advanced Usage: [Develop your own Task](customize-task.md).
* Advanced Usage: [Integrate with APScheduler](integrations/apscheduler.md).
* Advanced Usage: [Handle DateTime Objects](integrations/datetime.md).
* Internal: [Development](dev.md).

## Change Log

* See all changes: [Changelog](changelog.md).
