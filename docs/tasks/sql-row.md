# Sql Row Task

Sql Row Task enables fetching rows from a sql database, such as sqlite3, MySQL, PostgreSQL, MSSQL, etc.

The task type is "sql_row".

Added in v0.5.0.

## Example Usage

<<< @/examples/sqlite3_row.hcl

::: details Click me to view the run output
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
* `sql` - (Required, block) There can only be one sql blocks in a task.
  * `statement` - (Required, str) The sql statement to execute.
  * `parameters` - (Optional, list/map).
    * It can be a key-value pairs.
    * It can be a array of key-value pairs.

## Attributes References

The following attributes are supported:

* `rows` - List. Each list element is a map with table field as key and row record as value.
