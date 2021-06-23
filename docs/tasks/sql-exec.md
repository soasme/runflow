---
sidebar: auto
---

# Sql Exec Task

Sql Exec Task enables executing sql statements on a sql database, such as sqlite3, MySQL, PostgreSQL, MSSQL, etc.

The task type is "sql_exec".

Added in v0.5.0.

## Example Usage

<<< @/examples/sqlite3_exec.hcl

::: details Click me to view the run output
Run:

```
$ runflow run sqlite3_exec.hcl --var db=/tmp/out.db
[2021-06-12 23:02:04,386] "task.sqlite3_exec.create_table" is started.
[2021-06-12 23:02:04,390] "task.sqlite3_exec.create_table" is successful.
[2021-06-12 23:02:04,392] "task.sqlite3_exec.insert_many" is started.
[2021-06-12 23:02:04,393] "task.sqlite3_exec.insert_many" is successful.
[2021-06-12 23:02:04,394] "task.sqlite3_exec.insert_one" is started.
[2021-06-12 23:02:04,396] "task.sqlite3_exec.insert_one" is successful.

$ sqlite3 /tmp/out.db
SQLite version 3.32.3 2020-06-18 14:16:19
Enter ".help" for usage hints.
sqlite> select * from kvdb;
k1|v1
k2|v2
k3|v3
```
:::

## Argument Reference

:::tip
Please make sure you have the required driver package installed, such as MySQL-python or psycopg2.

Say you're using `postgresql` database, you can install `psycopg2`:

```bash
$ pip install psycopg2-binary
```
:::

The following arguments are supported:

* `dsn` - (Required, str) The DSN is a string of URL, which provides
  * What kind of database are we communicating with?
  * What DBAPI are we using?
  * How do we locate the database?

  Some examples include
  * `sqlite:///:memory:`,
  * `sqlite:////tmp/test.db`,
  * `sqlite+pysqlite:////tmp/test.db`,
  * `mysql://${var.mysql_user}:${var.mysql_pass}@${var.mysql_host}/${var.mysql_db}`,
  * `postgresql://scott:tiger@localhost/mydatabase`,
  * `postgresql+psycopg2://scott:tiger@localhost/mydatabase`,
  * `mssql+pymssql://scott:tiger@hostname:port/dbname`.

  Please see more examples [here](https://docs.sqlalchemy.org/en/14/core/engines.html).
* `sql` - (Required, block) There can be multiple sql blocks in a task.
  * `statement` - (Required, str) The sql statement to execute.
  * `parameters` - (Optional, list/map).
    * It can be a key-value pairs.
    * It can be a array of key-value pairs.
