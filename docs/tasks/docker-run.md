# Docker Run

Run a Docker container.

## Example Usage

* Set task type to "docker_run".
* Set docker image.
* Set the command.

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

* Set argument `environment` to key-value pairs.

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

## Set Entrypoint

* Set argument `entrypoint` to a list of strings.

<<< @/examples/docker-entrypoint.hcl

Run:

```
$ runflow run docker-entrypoint.hcl --var out=/tmp/out.txt
[2021-06-12 15:37:25,390] Task "setup" is started.
[2021-06-12 15:37:25,903] Task "setup" is successful.
[2021-06-12 15:37:25,906] Task "save" is started.
[2021-06-12 15:37:25,921] Task "save" is successful.

$ cat /tmp/out.txt
runflow is awesome
```

## Failed Execution

When the docker container exits with non-zero code, the task run is marked as failed.

<<< @/examples/docker-failed-run.hcl

Run:

```
$ runflow run examples/docker-failed-run.hcl
[2021-06-12 15:41:02,979] Task "exit" is started.
[2021-06-12 15:41:03,496] Task "exit" is failed.
Traceback (most recent call last):
... (truncated)
docker.errors.ContainerError: Command '/bin/bash -c 'exit 1'' in image 'ubuntu:latest' returned non-zero exit status 1: b''
```

If you want the task to keep running, please wrap up your script to recover the error.

## Full Arguments

Please refer to [docker.run parameters](https://docker-py.readthedocs.io/en/stable/containers.html#docker.models.containers.ContainerCollection.run).
