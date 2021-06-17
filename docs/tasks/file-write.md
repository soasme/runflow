# File Write Task

File Write task enables writing string content into a file.

Added in v0.3.0.

## Example Usage

Set attribute `filename` and `content`.

<<< @/examples/file_write.hcl

Run:

```bash
$ runflow run file_write.hcl
[2021-06-18 00:23:21,737] "task.file_write.this" is started.
[2021-06-18 00:23:21,740] "task.file_write.this" is successful.

$ cat /tmp/file_write.txt
foo bar
```

## Output Values to Terminal

Output values to terminal can be helpful on troubleshooting.

By using File Write Task with `"/dev/stdout"` as filename, you
can output the information to the terminal.

<<< @/examples/file_write_stdout.hcl

Run:

```
$ runflow run file_write_stdout.hcl
[2021-06-18 00:22:37,270] "task.file_write.this" is started.
{"web_proxy": {"proxy_host": "127.0.0.1", "proxy_port": 8964}}
[2021-06-18 00:22:37,270] "task.file_write.this" is successful.
```
