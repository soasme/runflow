---
sidebar: auto
---

# File Read Task

File Read task enables reading content from a file.

Added in v0.3.0.

Runflow supports various file systems by setting an optional `fs` attribute,
such as GitHub, FTP, SFTP, Arrow HDFS, HTTP, Zip, local Git repo, SMB, etc.
Check more information [here](https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations).

Added in v0.5.1.

## Example Usage

One can use `task.file_read.YOUR_TASK_NAME.content` in another task.

<<< @/examples/file_read.hcl

::: details Click me to view the run output
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
:::

## File Not Found

If `filename` is not a file or not found, an error occurs.

<<< @/examples/file_read_failed.hcl

::: details Click me to view the run output
Run:
```
$ runflow run file_read_failed.hcl
[2021-06-12 19:41:37,131] Task "this" is started.
[2021-06-12 19:41:37,132] Task "this" is failed.
Traceback (most recent call last):
... (truncated)
FileNotFoundError: [Errno 2] No such file or directory: '__nonexist__.toml'
```
:::


## Argument Reference

The following arguments are supported:

* `filename` - (Required, str) The path to file to read.
* `fs` - (Optional, map) The file system. If not set, local filesystem is used. Please check the filesystem for the arguments to set in the map:
  * [Local FileSystem](#local-filesystem)
  * [Git FileSystem](#git-filesystem)
  * [GitHub FileSystem](#github-filesystem)
  * More documentations for the other filesystems are on the way. :smile:

### Local FileSystem

This filesystem allows reading content from a local file.
If `fs` is not given, this filesystem is used by default.

* `protocol` - (Required, str) `"local"`.
* `auto_mkdir` - (Optional, bool) Whether to auto create the parent directories (if not exist) when opening a file.

Example usage:

<<< @/examples/file_read.hcl

::: details Click me to view the run output
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
:::

### GitHub FileSystem

This filesystem allows reading content from GitHub `org/repo`.

* `protocol` - (Required, str) `"github"`.
* `org` - (Required, str) The GitHub organization.
* `repo` - (Required, str) The GitHub repository.
* `sha` - (Optional, str) The Git SHA, such as git commit hash`d2f4db`, git tag `v0.5.0`, git branch `main`, etc.
* `username` - (Optional, str) The username for authorization.
* `token` - (Optional, str) The token for authorization. For accessing private repos, you must provide a token. The token can be made at <https://github.com/settings/tokens>.

Example usage:

This flow reads the content of file
[`"requirements-dev.txt"`](https://github.com/soasme/runflow/blob/v0.5.0/requirements-dev.txt)
from GitHub repo [soasme/runflow](https://github.com/soasme/runflow) with tag `v0.5.0`
and outputs to the console.

<<< @/examples/file_read_from_github.hcl

::: details Click me to view the run output
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
:::

### Git FileSystem

This filesystem allows reading content from a local Git repo.
The main difference between it and [Local FileSystem](#local-filesystem) is it
allows grabbing file content tracked in Git history.

* `protocol` - (Required, str) `"git"`.
* `path` - (Optional, str) The path to the local Git repo. Defaults to current directory if not given.
* `ref` - (Optional, str) The Git SHA, such as git commit hash`d2f4db`, git tag `v0.5.0`, git branch `main`, etc. Defaults to the current tree.

::: tip
The functionality requires installing package `pygit2`.
:::

For example, this flow reads "requirements-dev.txt" from the git repo.

<<< @/examples/file_read_from_git.hcl

::: details Click me to view the run output
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
:::
