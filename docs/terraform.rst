.. Terraform::

Terraform
=========

Shell Command as Job
--------------------

.. code-block::

    resource "jetflow_job" "my_shell_job" {
        schedule = "*/1 * * * *"
        shell {
            command = "echo `date` > /tmp/hello.txt"
        }
    }

Block `shell` supports `env`.

The executable must be available on the machine where Jetflow worker runs. 
The shell command will run in a separate process.

Python Module as Job
--------------------

.. code-block::

    resource "jetflow_job" "my_python_job" {
        schedule = "*/1 * * * *"
        module {
            package = "path.to.package"
            task = "TaskClass"
            kwargs = {"region": "us-west-2"}
            executor = "thread"
        }
    }

Block `module` guides how to construct a Task.

Docker Container as Job
-----------------------

.. code-block::

    resource "jetflow_job" "my_container_job" {
        schedule = "*/1 * * * *"
        container {
            image = "curlimages/curl:latest"
            options = "-L -v https://curl.haxx.se"
        }
    }

Block `container` defines necessary options for `podman run`.

ECS Task as Job
---------------

.. code-block::

    resource "jetflow_job" "my_ecs_job"
        schedule = "*/1 * * * *"
        ecs_task {
            container_definitions = jsonencode([
                # ...
            ])
        }
    }

Block `ecs_task` provides the AWS ECS task spec.
