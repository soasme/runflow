"""Run a flow spec."""

import asyncio

from .core import Flow
from .utils import import_module


def load_flow(path=None, source=None, module=None, flow=None):
    """Load a flow object."""
    if path:
        _flow = Flow.from_specfile(path)
    elif source:
        _flow = Flow.from_spec(source)
    elif module:
        _flow = import_module(module)
    elif flow:
        _flow = flow
    else:
        raise ValueError('Must provide one of path, source, module, flow')
    return _flow


def runflow(path=None, source=None, module=None, flow=None, vars=None):
    """Run a flow object."""
    _flow = load_flow(path=path, source=source, module=module, flow=flow)
    assert _flow and isinstance(_flow, Flow)
    coro = _flow.run(vars or {})
    asyncio.run(coro)
