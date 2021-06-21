class FileWriteTask:

    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    async def run(self, context):
        if self.filename == '/dev/stdout':
            print(str(self.content))
            return

        with open(self.filename, 'w+') as f:
            f.write(self.content)


class FileReadTask:

    def __init__(self, filename):
        self.filename = filename

    async def run(self, contenxt):
        with open(self.filename, 'r') as f:
            return {'content': f.read()}
