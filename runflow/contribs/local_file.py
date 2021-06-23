import fsspec


class FileWriteTask:
    def __init__(self, filename, content, fs=None):
        fs = fs if fs else {"protocol": "file"}
        self.filesystem = fsspec.filesystem(**fs)
        self.filename = filename
        self.content = content

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
        with self.filesystem.open(self.filename, "r") as file:
            return {"content": file.read()}
