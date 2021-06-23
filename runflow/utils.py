"""Utility functions."""

import sys
import asyncio
import importlib

def run_async(coro):
    if sys.version_info[0] == 3 and sys.version_info[1] < 7:
        loop = asyncio.get_running_loop()
        loop.run_until_complete(coro)
        return
    asyncio.run(coro)


async def to_thread(func, *args, **kwargs):
    """Run sync function in thread."""
    if sys.version_info[0] == 3 and sys.version_info[1] < 9:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: func(*args, **kwargs))

    return await asyncio.to_thread(func, *args, **kwargs)


def import_module(path):
    """Import a path like `path.to.module:class`."""
    try:
        package_name, module_name = path.split(':')
        result = importlib.import_module(package_name)
        getters = module_name.split('.')
        for getter in getters:
            result = getattr(result, getter)
        return result
    except (AttributeError, ValueError) as err:
        raise ImportError(path) from err


def split_camelcase(str):
    """Split WordLikeThis to ["Word", "Like", "This"]."""
    words = [[str[0]]]

    for char in str[1:]:
        if not words[-1][-1].isupper() and char.isupper():
            words.append(list(char))
        else:
            words[-1].append(char)

    return [''.join(word) for word in words]
