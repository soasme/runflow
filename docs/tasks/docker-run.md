# Docker Run

Run a Docker container.

## Example Usage

<<< @/examples/docker-hello-world.hcl

Run:

```
$ runflow run docker-hello-world.hcl --var out=/tmp/out.txt
[2021-06-12 15:14:01,654] Task "echo" is started.
[2021-06-12 15:14:02,158] Task "echo" is successful.
[2021-06-12 15:14:02,160] Task "save" is started.
[2021-06-12 15:14:02,234] Task "save" is successful.
```
