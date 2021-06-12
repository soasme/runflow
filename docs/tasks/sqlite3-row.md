# Sqlite3 Row Task

Sqlite3 Row Task enables fetching rows from a sqlite3 db.

The Task type is "sqlite3_row".

Added in v0.4.0.

## Example Usage

* Provide dsn, sql and parameter (optional).
* If one single row is expected, set exec_many to false to speed up the performance.

<<< @/examples/sqlite3_example.hcl

Run:

```
$ runflow run sqlite3_example.hcl --var db=/tmp/out.db
[2021-06-12 23:06:07,567] "task.sqlite3_exec.create_table" is started.
[2021-06-12 23:06:07,571] "task.sqlite3_exec.create_table" is successful.
[2021-06-12 23:06:07,573] "task.sqlite3_exec.insert_many" is started.
[2021-06-12 23:06:07,574] "task.sqlite3_exec.insert_many" is successful.
[2021-06-12 23:06:07,576] "task.sqlite3_exec.insert_one" is started.
[2021-06-12 23:06:07,577] "task.sqlite3_exec.insert_one" is successful.
[2021-06-12 23:06:07,578] "task.sqlite3_row.k1" is started.
[2021-06-12 23:06:07,578] "task.sqlite3_row.k1" is successful.
[2021-06-12 23:06:07,580] "task.command.print_k1" is started.
k1: v1
[2021-06-12 23:06:07,593] "task.command.print_k1" is successful.
[2021-06-12 23:06:07,594] "task.sqlite3_row.kall" is started.
[2021-06-12 23:06:07,595] "task.sqlite3_row.kall" is successful.
[2021-06-12 23:06:07,597] "task.template.kall" is started.
[2021-06-12 23:06:07,597] "task.template.kall" is successful.
[2021-06-12 23:06:07,597] "task.command.print_all" is started.
[[k1, v1], [k2, v2], [k3, v3]]
[2021-06-12 23:06:07,609] "task.command.print_all" is successful.
```
