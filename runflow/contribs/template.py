class Hcl2TemplateTask:
    def __init__(self, source, context=None):
        self.source = source

    async def run(self):
        return {"content": self.source}
