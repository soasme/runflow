# File Read Task

File Read task enables reading content from a file.

## Example Usage

One can use `task.file_read.YOUR_TASK_NAME.content` in another task.

<<< @/examples/file_read.hcl

Run:

```
$ runflow run file_read.hcl
[2021-06-12 19:40:56,276] Task "this" is started.
[2021-06-12 19:40:56,279] Task "this" is successful.
[2021-06-12 19:40:56,281] Task "this" is started.
"[build-system]
requires = [
    \"setuptools\u003e=42\",
    \"wheel\"
]
build-backend = \"setuptools.build_meta\"
"
[2021-06-12 19:40:56,292] Task "this" is successful.
```

## File Not Found

If `filename` is not a file or not found, an error occurs.

<<< @/examples/file_read_failed.hcl

Run:

```
$ runflow run file_read_failed.hcl
[2021-06-12 19:41:37,131] Task "this" is started.
[2021-06-12 19:41:37,132] Task "this" is failed.
Traceback (most recent call last):
... (truncated)
FileNotFoundError: [Errno 2] No such file or directory: '__nonexist__.toml'
```

