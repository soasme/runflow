from aiofile import async_open


class LocalFileWriteTask:

    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    async def run(self, context):
        async with async_open(self.filename, 'w+') as f:
            await f.write(self.content)


class LocalFileReadTask:

    def __init__(self, filename):
        self.filename = filename

    async def run(self, contenxt):
        async with async_open(self.filename, 'r') as f:
            return {
                'content': await f.read()
            }
