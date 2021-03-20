.. Terraform::

Terraform
=========

Shell Command as Job
--------------------

Block `shell` defines how to run a command.

.. code-block::

    resource "jetflow_job" "my_shell_job" {
        schedule = "*/1 * * * *"
        shell {
            command = "echo `date` > /tmp/hello.txt"
            env = "PATH=/usr/bin"
        }
    }


The executable must be available on the machine where Jetflow worker runs. 
The shell command will run in a separate process.

Python Module as Job
--------------------

Block `module` guides how to construct a Task.

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


Docker Container as Job
-----------------------

Block `container` defines necessary options for `podman run`.

.. code-block::

    resource "jetflow_job" "my_container_job" {
        schedule = "*/1 * * * *"
        container {
            image = "curlimages/curl:latest"
            options = "-L -v https://curl.haxx.se"
        }
    }


ECS Task as Job
---------------

Block `ecs_task` provides the AWS ECS task spec.

.. code-block::

    resource "jetflow_job" "my_ecs_job"
        schedule = "*/1 * * * *"
        ecs_task {
            container_definitions = jsonencode([
                # ...
            ])
        }
    }


Lambda Function as Job
-----------------------

Block `lambda_function` provides the AWS Lambda Function spec.

.. code-block::

    resource "jetflow_job" "my_ecs_job"
        schedule = "*/1 * * * *"
        lambda_function {
        }
    }


Vercel Function as Job
-----------------------

Block `lambda_function` provides the AWS Lambda Function spec.

.. code-block::

    resource "jetflow_job" "my_ecs_job"
        schedule = "*/1 * * * *"
        lambda_function {
        }
    }

