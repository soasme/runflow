---
sidebar: auto
---

# Bash Run Task

Bash Run task enables running local command in a subprocess.

## Example Usage

<<< @/examples/hello-id.hcl

## Optional Environment Variables

Command task supports optional environment variables through argument `env`.

<<< @/examples/hello-id-env.hcl

Whenever possible, instead of templating variables in the command, pass variables into the command using `env`.
(Bash is quite tricky in some circumstances).

## Argument Reference

The following arguments are supported:

* `command` - (Required, str) The command string.
* `env` - (Optional, map) The environment variables.

## Attributes Reference

The following attributes are supported:

* `stdout` - String. The output of command run.
* `stderr` - String. The error of command run.
* `returncode` - Int. The exit code of command run.
