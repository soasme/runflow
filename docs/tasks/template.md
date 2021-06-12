# Template Task

Template task enables rendering source with given context.

## Example Usage

<<< @/examples/template.hcl

Run:

```
$ runflow run template.hcl --var out=/tmp/out.txt
[2021-06-12 20:19:34,003] "task.template.this" is started.
[2021-06-12 20:19:34,003] "task.template.this" is successful.
[2021-06-12 20:19:34,017] "task.file_write.this" is started.
[2021-06-12 20:19:34,022] "task.file_write.this" is successful.

$ cat /tmp/out.txt
42
42
/tmp/out.txt
```
