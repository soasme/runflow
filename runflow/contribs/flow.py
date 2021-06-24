from runflow import loadflow


class FlowRunTask:
    def __init__(self, path=None, source=None, module=None, vars=None):
        self.flow = loadflow(path=path, source=source, module=module)
        self.vars = vars or {}

    async def run(self, context):
        await self.flow.run(vars=self.vars)
