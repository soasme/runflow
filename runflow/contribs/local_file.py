from aiofile import async_open

class LocalFileWriteTask:

    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    async def run(self, context):
        async with async_open(self.filename, 'w+') as f:
            await f.write(self.content)
