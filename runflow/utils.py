import sys
import asyncio
import importlib


async def to_thread(f, *args, **kwargs):
    if sys.version_info[0] == 3 and sys.version_info[1] < 9:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: f(*args, **kwargs))

    return await asyncio.to_thread(f, *args, **kwargs)


def import_module(path):
    try:
        package_name, module_name = path.split(':')
        result = importlib.import_module(package_name)
        getters = module_name.split('.')
        for getter in getters:
            result = getattr(result, getter)
        return result
    except (AttributeError, ValueError):
        raise ImportError(path)


def split_camelcase(str):
    words = [[str[0]]]

    for c in str[1:]:
        if not words[-1][-1].isupper() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    return [''.join(word) for word in words]
