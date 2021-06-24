from runflow import loadflow
from runflow.hcl2 import loads, evaluate


class FlowRunTask:
    def __init__(
        self, path=None, source=None, module=None, vars=None, exports=None
    ):
        self.flow = loadflow(path=path, source=source, module=module)
        self.vars = vars or {}
        self.exports = exports or {}

    async def run(self, context):
        flow_context = await self.flow.run(vars=self.vars)
        return {
            key: evaluate(loads(value, "eval"), flow_context)
            for key, value in self.exports.items()
        }
