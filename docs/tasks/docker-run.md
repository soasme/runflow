---
sidebar: auto
---

# Docker Run

Run a Docker container.

This feature requires `runflow[docker]`.

```
$ pip install runflow[docker]
```

Added in v0.3.0.

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
docker.errors.ContainerError: Command "/bin/bash -c 'exit 1'" in image 'ubuntu:latest' returned non-zero exit status 1: b''
```

If you want the task to keep running, please wrap up your script to recover the error.

## Argument Reference

The following arguments are supported:

*   **image** (_str_) – The image to run.
*   **command** (_str or list_) – The command to run in the container.
*   **auto\_remove** (_bool_) – enable auto-removal of the container on daemon side when the container’s process exits.
*   **blkio\_weight\_device** – Block IO weight (relative device weight) in the form of: `[{"Path": "device_path", "Weight": weight}]`.
*   **blkio\_weight** – Block IO weight (relative weight), accepts a weight value between 10 and 1000.
*   **cap\_add** (_list of str_) – Add kernel capabilities. For example, `["SYS_ADMIN", "MKNOD"]`.
*   **cap\_drop** (_list of str_) – Drop kernel capabilities.
*   **cgroup\_parent** (_str_) – Override the default parent cgroup.
*   **cpu\_count** (_int_) – Number of usable CPUs (Windows only).
*   **cpu\_percent** (_int_) – Usable percentage of the available CPUs (Windows only).
*   **cpu\_period** (_int_) – The length of a CPU period in microseconds.
*   **cpu\_quota** (_int_) – Microseconds of CPU time that the container can get in a CPU period.
*   **cpu\_rt\_period** (_int_) – Limit CPU real-time period in microseconds.
*   **cpu\_rt\_runtime** (_int_) – Limit CPU real-time runtime in microseconds.
*   **cpu\_shares** (_int_) – CPU shares (relative weight).
*   **cpuset\_cpus** (_str_) – CPUs in which to allow execution (`0-3`, `0,1`).
*   **cpuset\_mems** (_str_) – Memory nodes (MEMs) in which to allow execution (`0-3`, `0,1`). Only effective on NUMA systems.
*   **detach** (_bool_) – Run container in the background and return a [`Container`](#docker.models.containers.Container "docker.models.containers.Container") object.
*   **device\_cgroup\_rules** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – A list of cgroup rules to apply to the container.
*   **device\_read\_bps** – Limit read rate (bytes per second) from a device in the form of: \[{“Path”: “device\_path”, “Rate”: rate}\]
*   **device\_read\_iops** – Limit read rate (IO per second) from a device.
*   **device\_write\_bps** – Limit write rate (bytes per second) from a device.
*   **device\_write\_iops** – Limit write rate (IO per second) from a device.
*   **devices** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) –
    
    Expose host devices to the container, as a list of strings in the form `<path_on_host>:<path_in_container>:<cgroup_permissions>`.
    
    For example, `/dev/sda:/dev/xvda:rwm` allows the container to have read-write access to the host’s `/dev/sda` via a node named `/dev/xvda` inside the container.
    
*   **device\_requests** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – Expose host resources such as GPUs to the container, as a list of `docker.types.DeviceRequest` instances.
*   **dns** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – Set custom DNS servers.
*   **dns\_opt** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – Additional options to be added to the container’s `resolv.conf` file.
*   **dns\_search** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – DNS search domains.
*   **domainname** (_str or list_) – Set custom DNS search domains.
*   **entrypoint** (_str or list_) – The entrypoint for the container.
*   **environment** (_map or list_) – Environment variables to set inside the container, as a map or a list of strings in the format `["SOMEVARIABLE=xxx"]`.
*   **extra\_hosts** (_map_) – Additional hostnames to resolve inside the container, as a mapping of hostname to IP address.
*   **group\_add** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – List of additional group names and/or IDs that the container process will run as.
*   **healthcheck** (_map_) – Specify a test to perform to check that the container is healthy.
*   **hostname** (_str_) – Optional hostname for the container.
*   **init** (_bool_) – Run an init inside the container that forwards signals and reaps processes
*   **init\_path** (_str_) – Path to the docker-init binary
*   **ipc\_mode** (_str_) – Set the IPC mode for the container.
*   **isolation** (_str_) – Isolation technology to use. Default: None.
*   **kernel\_memory** (_int or str_) – Kernel memory limit
*   **labels** (_map or list_) – A map of name-value labels (e.g. `{"label1": "value1", "label2": "value2"}`) or a list of names of labels to set with empty values (e.g. `["label1", "label2"]`)
*   **links** (_map_) – Mapping of links using the `{"container": "alias"}` format. The alias is optional. Containers declared in this map will be linked to the new container using the provided alias. Default: `None`.
*   **log\_config** ([_LogConfig_](api.html#docker.types.LogConfig "docker.types.LogConfig")) – Logging configuration.
*   **lxc\_conf** (_map_) – LXC config.
*   **mac\_address** (_str_) – MAC address to assign to the container.
*   **mem\_limit** (_int or str_) – Memory limit. Accepts float values (which represent the memory limit of the created container in bytes) or a string with a units identification char (`100000b`, `1000k`, `128m`, `1g`). If a string is specified without a units character, bytes are assumed as an intended unit.
*   **mem\_reservation** (_int or str_) – Memory soft limit.
*   **mem\_swappiness** (_int_) – Tune a container’s memory swappiness behavior. Accepts number between 0 and 100.
*   **memswap\_limit** (_str or int_) – Maximum amount of memory + swap a container is allowed to consume.
*   **mounts** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – Specification for mounts to be added to the container. More powerful alternative to `volumes`. Each item in the list is expected to be a [`docker.types.Mount`](api.html#docker.types.Mount "docker.types.Mount") object.
*   **name** (_str_) – The name for this container.
*   **nano\_cpus** (_int_) – CPU quota in units of 1e-9 CPUs.
*   **network** (_str_) – Name of the network this container will be connected to at creation time. You can connect to additional networks using `Network.connect()`. Incompatible with `network_mode`.
*   **network\_disabled** (_bool_) – Disable networking.
*   **network\_mode** (_str_) –
    
    One of:
    
    *   `bridge` Create a new network stack for the container on on the bridge network.
    *   `none` No networking for this container.
    *   `container:<name|id>` Reuse another container’s network stack.
    *   `host` Use the host network stack. This mode is incompatible with `ports`.
    
    Incompatible with `network`.
    
*   **oom\_kill\_disable** (_bool_) – Whether to disable OOM killer.
*   **oom\_score\_adj** (_int_) – An integer value containing the score given to the container in order to tune OOM killer preferences.
*   **pid\_mode** (_str_) – If set to `host`, use the host PID namespace inside the container.
*   **pids\_limit** (_int_) – Tune a container’s pids limit. Set `-1` for unlimited.
*   **platform** (_str_) – Platform in the format `os[/arch[/variant]]`. Only used if the method needs to pull the requested image.
*   **ports** (_map_) –
    
    Ports to bind inside the container.
    
    The keys of the map are the ports to bind inside the container, either as an integer or a string in the form `port/protocol`, where the protocol is either `tcp`, `udp`, or `sctp`.
    
    The values of the map are the corresponding ports to open on the host, which can be either:
    
    *   The port number, as an integer. For example, `{"2222/tcp": 3333}` will expose port 2222 inside the container as port 3333 on the host.
    *   `None`, to assign a random host port. For example, `{"2222/tcp": None}`.
    *   A tuple of `(address, port)` if you want to specify the host interface. For example, `{"1111/tcp": ("127.0.0.1", 1111)}`.
    *   A list of integers, if you want to bind multiple host ports to a single container port. For example, `{"1111/tcp": [1234, 4567]}`.
    
    Incompatible with `host` network mode.
    
*   **privileged** (_bool_) – Give extended privileges to this container.
*   **publish\_all\_ports** (_bool_) – Publish all ports to the host.
*   **read\_only** (_bool_) – Mount the container’s root filesystem as read only.
*   **remove** (_bool_) – Remove the container when it has finished running. Default: `False`.
*   **restart\_policy** (_map_) –
    
    Restart the container when it exits. Configured as a map with keys:
    
    *   `Name` One of `on-failure`, or `always`.
    *   `MaximumRetryCount` Number of times to restart the container on failure.
    
    For example: `{"Name": "on-failure", "MaximumRetryCount": 5}`
    
*   **runtime** (_str_) – Runtime to use with this container.
*   **security\_opt** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – A list of string values to customize labels for MLS systems, such as SELinux.
*   **shm\_size** (_str or int_) – Size of /dev/shm (e.g. `1G`).
*   **stdin\_open** (_bool_) – Keep `STDIN` open even if not attached.
*   **stdout** (_bool_) – Return logs from `STDOUT` when `detach=False`. Default: `True`.
*   **stderr** (_bool_) – Return logs from `STDERR` when `detach=False`. Default: `False`.
*   **stop\_signal** (_str_) – The stop signal to use to stop the container (e.g. `SIGINT`).
*   **storage\_opt** (_map_) – Storage driver options per container as a key-value mapping.
*   **stream** (_bool_) – If true and `detach` is false, return a log generator instead of a string. Ignored if `detach` is true. Default: `False`.
*   **sysctls** (_map_) – Kernel parameters to set in the container.
*   **tmpfs** (_map_) –
    
    Temporary filesystems to mount, as a map mapping a path inside the container to options for that path.
    
    For example:
    
        {
            "/mnt/vol2": "",
            "/mnt/vol1": "size=3G,uid=1000"
        }
    
*   **tty** (_bool_) – Allocate a pseudo-TTY.
*   **ulimits** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – Ulimits to set inside the container, as a list of [`docker.types.Ulimit`](api.html#docker.types.Ulimit "docker.types.Ulimit") instances.
*   **use\_config\_proxy** (_bool_) – If `True`, and if the docker client configuration file (`~/.docker/config.json` by default) contains a proxy configuration, the corresponding environment variables will be set in the container being built.
*   **user** (_str or int_) – Username or UID to run commands as inside the container.
*   **userns\_mode** (_str_) – Sets the user namespace mode for the container when user namespace remapping option is enabled. Supported values are: `host`
*   **uts\_mode** (_str_) – Sets the UTS namespace mode for the container. Supported values are: `host`
*   **version** (_str_) – The version of the API to use. Set to `auto` to automatically detect the server’s version. Default: `1.35`
*   **volume\_driver** (_str_) – The name of a volume driver/plugin.
*   **volumes** (_map or list_) –

    A map to configure volumes mounted inside the container. The key is either the host path or a volume name, and the value is a map with the keys:

    *   `bind` The path to mount the volume inside the container
    *   `mode` Either `rw` to mount the volume read/write, or `ro` to mount it read-only.

    For example:

         {"/home/user1/": {"bind": "/mnt/vol2", "mode": "rw"},
         "/var/www": {"bind": "/mnt/vol1", "mode": "ro"}}

*   **volumes\_from** ([`list`](#docker.models.containers.ContainerCollection.list "docker.models.containers.ContainerCollection.list")) – List of container names or IDs to get volumes from.
*   **working\_dir** (_str_) – Path to the working directory.

## Attributes Reference

The following attributes are supported:

* `stdout` - String. The output of command run.
