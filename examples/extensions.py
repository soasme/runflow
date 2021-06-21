class GuessIceCreamTask:

    def __init__(self, name, output):
        self.name = name
        self.output = output

    async def run(self, context):
        with open(self.output, 'w') as f:
            f.write(f"Bingo, it is {self.name}")
