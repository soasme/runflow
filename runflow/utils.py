"""Utility functions."""

import asyncio
import importlib
import sys


def run_async(coro):
    """Wrap async function as sync call."""
    if sys.version_info[0] == 3 and sys.version_info[1] < 7:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(coro)
        return
    asyncio.run(coro)


async def to_thread(func, *args, **kwargs):
    """Run sync function in thread."""
    if sys.version_info[0] == 3 and sys.version_info[1] < 9:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: func(*args, **kwargs))

    # pylint: disable=no-member
    return await asyncio.to_thread(func, *args, **kwargs)


def import_module(path):
    """Import a path like `path.to.module:class`."""
    try:
        package_name, module_name = path.split(":")
        result = importlib.import_module(package_name)
        getters = module_name.split(".")
        for getter in getters:
            result = getattr(result, getter)
        return result
    except (AttributeError, ValueError) as err:
        raise ImportError(path) from err
