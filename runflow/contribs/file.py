from base64 import b64decode, b64encode
from typing import Optional

import attr
import fsspec


@attr.s(
    auto_attribs=True,
    kw_only=True,
    frozen=True,
)
class FileWriteTask:
    """This task write the file cotnent to the supported file system."""

    filename: str = attr.ib(
        validator=attr.validators.instance_of(str),
    )
    fs: dict = attr.ib(  # pylint: disable=invalid-name
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )
    content: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)),
        default=None,
    )
    b64content: Optional[bytes] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(bytes)),
        default=None,
    )

    async def run(self):
        content = (
            b64decode(self.b64content) if self.b64content else self.content
        )

        if self.filename == "/dev/stdout":
            print(str(content))
            return

        filesystem = fsspec.filesystem(
            **(self.fs if self.fs else {"protocol": "file"})
        )
        bcontent = (
            content if isinstance(content, bytes) else content.encode("utf-8")
        )

        with filesystem.open(self.filename, "wb") as file:
            file.write(bcontent)


@attr.s(
    auto_attribs=True,
    kw_only=True,
    frozen=True,
)
class FileReadTask:
    """This task read the file content from the supported file system."""

    filename: str = attr.ib(
        validator=attr.validators.instance_of(str),
    )
    fs: dict = attr.ib(  # pylint: disable=invalid-name
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )

    async def run(self):
        filesystem = fsspec.filesystem(
            **(self.fs if self.fs else {"protocol": "file"})
        )
        with filesystem.open(self.filename, "rb") as file:
            content = file.read()
            return {
                "content": content.decode("utf-8"),
                "b64content": b64encode(content).decode("utf-8"),
            }
