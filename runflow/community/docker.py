try:
    import docker
except ImportError:
    print("Please install Python package `docker` to use `docker_run` task.")
    docker = None

from runflow.utils import to_thread


class DockerRunTask:
    def __init__(self, image, command=None, **kwargs):
        self.image = image
        self.command = command
        self.args = kwargs
        self.client = docker.from_env()

    async def run(self):
        stdout = await to_thread(
            self.client.containers.run,
            image=self.image,
            command=self.command,
            detach=False,
            remove=True,
            **self.args
        )
        return {
            "stdout": stdout.decode("utf-8").strip(),
        }
