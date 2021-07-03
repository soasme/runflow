import asyncio

from runflow.errors import RunflowTaskError


class BashRunTask:
    def __init__(self, command, env=None):
        self.command = command
        env = env or {}
        self.env = {k: str(v) for k, v in env.items()}

    async def run(self):
        proc = await asyncio.create_subprocess_shell(
            self.command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=self.env,
        )

        stdout, stderr = await proc.communicate()
        stdout = stdout.decode("utf-8").strip()
        stderr = stderr.decode("utf-8").strip()

        if stdout:
            print(stdout)

        if proc.returncode == 0:
            return dict(
                returncode=proc.returncode,
                stdout=stdout,
                stderr=stderr,
            )

        raise RunflowTaskError(
            dict(
                returncode=proc.returncode,
                stdout=stdout,
                stderr=stderr,
            )
        )
