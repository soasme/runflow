from aiofile import async_open

class GuessIceCreamTask:

    def __init__(self, name, output):
        self.name = name
        self.output = output

    async def run(self, context):
        async with async_open(self.output, 'w+') as f:
            await f.write(f"bingo, it is {self.name}")
