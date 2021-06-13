class TemplateTask:

    def __init__(self, source, context=None):
        self.source = source

    async def run(self, context):
        return {'content': self.source}
