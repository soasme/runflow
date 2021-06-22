# File Read Task

File Read task enables reading content from a file.

Added in v0.3.0.

Runflow supports various file system by setting an optional `fs` attribute,
such as GitHub, FTP, SFTP, Arrow HDFS, HTTP, Zip, local Git repo, SMB, etc.
Check more information [here](https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations).

Added in v0.5.1.

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

## Read File Content From GitHub

To read file content from GitHub, set `fs.protocol` is `"github"`.

For example, this flow reads "requirements-dev.txt" from
<https://github.com/soasme/runflow/blob/v0.5.0/requirements-dev.txt>.

<<< @/examples/file_read_from_github.hcl

Run:

```
$ runflow run examples/file_read_from_github.hcl
[2021-06-22 16:09:07,594] "task.file_read.this" is started.
[2021-06-22 16:09:08,069] "task.file_read.this" is successful.
[2021-06-22 16:09:08,070] "task.file_write.this" is started.
build
twine
pytest
pytest-cov
[2021-06-22 16:09:08,071] "task.file_write.this" is successful.
```

## Read File Content From Local Git Repo

To read file content from GitHub, set `fs.protocol` is `"git"`.
This functionality requires installing package `pygit2`.

For example, this flow reads "requirements-dev.txt" from the git repo.

<<< @/examples/file_read_from_git.hcl

Run:

```
$ pip install pygit2

$ runflow run examples/file_read_from_git.hcl
[2021-06-22 16:15:01,124] "task.file_read.this" is started.
[2021-06-22 16:15:01,127] "task.file_read.this" is successful.
[2021-06-22 16:15:01,128] "task.file_write.this" is started.
build
twine
pytest
pytest-cov
[2021-06-22 16:15:01,129] "task.file_write.this" is successful.
```
