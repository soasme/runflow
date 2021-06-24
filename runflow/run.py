"""Run a flow spec."""

from .core import Flow
from .utils import import_module, run_async


def loadflow(path=None, source=None, module=None, flow=None):
    """Load a flow object."""
    if path:
        flow = Flow.from_specfile(path)
    elif source:
        flow = Flow.from_spec(source)
    elif module:
        flow = import_module(module)
    return flow


async def runflow_async(
    path=None, source=None, module=None, flow=None, vars=None
):
    """Run a flow object (async)."""
    _flow = loadflow(path=path, source=source, module=module, flow=flow)
    assert _flow and isinstance(_flow, Flow)
    await _flow.run(vars or {})


def runflow(path=None, source=None, module=None, flow=None, vars=None):
    """Run a flow object (sync)."""
    run_async(
        runflow_async(
            path=path, source=source, module=module, flow=flow, vars=vars
        )
    )
