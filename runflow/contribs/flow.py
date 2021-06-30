from runflow import loadflow
from runflow.hcl2 import loads, evaluate


class FlowRunTask:
    def __init__(
        self, path=None, source=None, module=None, vars=None, exports=None
    ):
        self.path = path
        self.source = source
        self.module = module
        self.vars = vars or {}
        self.exports = exports or {}

    async def run(self, context):
        flow = loadflow(path=self.path, source=self.source, module=self.module)
        flow_context = await flow.run(vars=self.vars)

        if flow.exception:
            raise flow.exception

        return {
            key: evaluate(loads(value, "eval"), flow_context)
            for key, value in self.exports.items()
        }
