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

    async def run(self, context):
        if self.filename == "/dev/stdout":
            print(str(self.content))
            return

        with self.filesystem.open(self.filename, "w+") as file:
            file.write(self.content)


class FileReadTask:
    def __init__(self, filename, fs=None):
        fs = fs if fs else {"protocol": "file"}
        self.filesystem = fsspec.filesystem(**fs)
        self.filename = filename

    async def run(self, contenxt):
        with self.filesystem.open(self.filename, "rb") as file:
            content = file.read()
            return {
                "content": content.decode("utf-8"),
                "b64content": b64encode(content),
            }
