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

$ cat /tmp/out.txt
hello world
```

## Set Environment Variables

<<< @/examples/docker-env.hcl

Run:

```
$ runflow run docker-env.hcl --var out=/tmp/out.txt
[2021-06-12 15:24:08,870] Task "echo" is started.
[2021-06-12 15:24:09,399] Task "echo" is successful.
[2021-06-12 15:24:09,401] Task "save" is started.
[2021-06-12 15:24:09,415] Task "save" is successful.

$ cat /tmp/out.txt
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=9389736c56f1
greeter=world
HOME=/root
```
