# Sqlite3 Row Task

Sqlite3 Row Task enables fetching rows from a sql database, such as sqlite3, mysql, postgres, etc.

The Task type is "sql_row".

Added in v0.5.0.

## Example Usage

<<< @/examples/sqlite3_row.hcl

Run:

```
$ rm -rf /tmp/sqlite3.db
$ sqlite3 /tmp/sqlite3.db "create table kvdb (key string primary key, value string);'
$ sqlite3 /tmp/sqlite3.db "insert into kvdb (key, value) values ('k1','v1'),('k2','v2'),('k3','v3');"

$ runflow run sqlite3_row.hcl --var db=/tmp/out.db
[2021-06-12 23:25:56,188] "task.sqlite3_row.k1" is started.
[2021-06-12 23:25:56,191] "task.sqlite3_row.k1" is successful.
[2021-06-12 23:25:56,192] "task.sqlite3_row.kall" is started.
[2021-06-12 23:25:56,193] "task.sqlite3_row.kall" is successful.
[2021-06-12 23:25:56,195] "task.command.echo" is started.
{"k1": [{"key": "k1", "value": "v1"}], "kall": [{"key": "k1", "value": "v1"}, {"key": "k2", "value": "v2"}, {"key": "k3", "value": "k3"}]}
[2021-06-12 23:25:56,207] "task.command.echo" is successful.
```

## Task Spec

The task body requires:

* Attribute `dsn`. The DSN is a string of URL, which provides
  * What kind of database are we communicating with?
  * What DBAPI are we using?
  * How do we locate the database?
  Some examples include
  * `sqlite:///:memory:`
  * `sqlite:////tmp/test.db`
  * `sqlite+pysqlite:////tmp/test.db`
  * `mysql://${var.mysql_user}:${var.mysql_pass}@${var.mysql_host}/${var.mysql_db}`
  * Please see more examples [here](https://docs.sqlalchemy.org/en/14/core/engines.html) and have driver package like MySQL-python or psycopg2 installed.
* Block `sql`. There can only be one sql blocks in a task.
  * Attribute `statement`, the sql statement to execute.
  * Attribute `parameters` (optional).
    * It can be a key-value pairs.
    * It can be a array of key-value pairs.
