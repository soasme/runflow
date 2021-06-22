from runflow.core import load_flow


class FlowRunTask:

    def __init__(self, path=None, source=None, module=None, vars=None):
        self.flow = load_flow(path=path, source=source, module=module)
        self.vars = vars or {}

    async def run(self, context):
        await self.flow.run(vars=self.vars)
