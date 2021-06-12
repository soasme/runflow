class TemplateTask:

    def __init__(self, source):
        self.source = source

    async def run(self, context):
        return {'content': self.source}
