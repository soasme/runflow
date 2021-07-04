"""Run a flow spec."""

from .core import Flow
from .utils import run_async


async def runflow_async(
    path=None, source=None, module=None, flow=None, vars=None
):
    """Run a flow object (async)."""
    _flow = Flow.load(path=path, source=source, module=module, flow=flow)
    assert _flow and isinstance(_flow, Flow)
    await _flow.run(vars or {})


def runflow(path=None, source=None, module=None, flow=None, vars=None):
    """Run a flow object (sync)."""
    run_async(
        runflow_async(
            path=path, source=source, module=module, flow=flow, vars=vars
        )
    )
