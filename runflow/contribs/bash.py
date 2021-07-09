import sys
import asyncio
from typing import Dict

import attr

from runflow.errors import RunflowTaskError
from runflow.utils import RunflowValidators


@attr.s(
    auto_attribs=True,
    kw_only=True,
    frozen=True,
)
class BashRunTask:

    command: str = attr.ib(
        default="",
        validator=[
            attr.validators.instance_of(str),
            RunflowValidators.not_empty,
        ],
    )
    env: Dict[str, str] = attr.ib(
        factory=dict,
    )

    async def run(self):
        proc = await asyncio.create_subprocess_shell(
            self.command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env={k: str(v) for k, v in self.env.items()},
        )

        stdout, stderr = await proc.communicate()
        stdout = stdout.decode("utf-8").strip()
        stderr = stderr.decode("utf-8").strip()

        if stdout:
            sys.stdout.write(stdout)
            if not stdout.endswith("\n"):
                sys.stdout.write("\n")
            sys.stdout.flush()

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
