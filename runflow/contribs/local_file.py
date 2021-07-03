from base64 import b64decode, b64encode

import fsspec


class FileWriteTask:
    def __init__(self, filename, content=None, b64content=None, fs=None):
        fs = fs if fs else {"protocol": "file"}
        self.filesystem = fsspec.filesystem(**fs)
        self.filename = filename
        if content is not None:
            self.content = content
        elif b64content is not None:
            self.content = b64decode(b64content)
        else:
            raise ValueError(
                "at least one of `content` / `b64content` must have value"
            )

    async def run(self):
        if self.filename == "/dev/stdout":
            print(str(self.content))
            return

        content = (
            self.content
            if isinstance(self.content, bytes)
            else self.content.encode("utf-8")
        )

        with self.filesystem.open(self.filename, "wb") as file:
            file.write(content)


class FileReadTask:
    def __init__(self, filename, fs=None):
        fs = fs if fs else {"protocol": "file"}
        self.filesystem = fsspec.filesystem(**fs)
        self.filename = filename

    async def run(self):
        with self.filesystem.open(self.filename, "rb") as file:
            content = file.read()
            return {
                "content": content.decode("utf-8"),
                "b64content": b64encode(content).decode("utf-8"),
            }
