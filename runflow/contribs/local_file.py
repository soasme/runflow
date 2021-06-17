from aiofile import async_open


class FileWriteTask:

    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    async def run(self, context):
        if self.filename == '/dev/stdout':
            print(str(self.content))
            return

        async with async_open(self.filename, 'w+') as f:
            await f.write(self.content)


class FileReadTask:

    def __init__(self, filename):
        self.filename = filename

    async def run(self, contenxt):
        async with async_open(self.filename, 'r') as f:
            return {
                'content': await f.read()
            }
