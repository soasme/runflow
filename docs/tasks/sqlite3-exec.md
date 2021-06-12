# Sqlite3 Exec Task

Sqlite3 Exec Task enables executing a sql statement on a sqlite3 db.

## Example Usage

Provide dsn, sql and parameters (optional).

The dsn should be valid filepath of a sqlite db.

<<< @/examples/sqlite3_exec.hcl

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
