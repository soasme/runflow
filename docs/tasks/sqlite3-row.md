# Sqlite3 Row Task

Sqlite3 Row Task enables fetching rows from a sqlite3 db.

The Task type is "sqlite3_row".

Added in v0.4.0.

## Example Usage

* Provide dsn, sql and parameter (optional).
* If one single row is expected, set exec_many to false to speed up the performance.

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
k1: v1
kall: [["k1", "v1"], ["k2", "v2"], ["k3", "v3"]]
[2021-06-12 23:25:56,207] "task.command.echo" is successful.
```
