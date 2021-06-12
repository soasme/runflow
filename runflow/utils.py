import sys
import asyncio

import jinja2

def render(source, context):
    if isinstance(source, str):
        tpl = jinja2.Template(
            source,
            variable_start_string="${",
            variable_end_string="}",
            undefined=jinja2.StrictUndefined,
        )
        return tpl.render(context)
    elif isinstance(source, list):
        return [render(s, context) for s in source]
    elif isinstance(source, dict):
        return {k: render(v, context) for k, v in source.items()}
    elif isinstance(source, int):
        return source
    else:
        raise ValueError(f"Invalid template source: {source}")

async def to_thread(f, *args, **kwargs):
    if sys.version_info[0] == 3 and sys.version_info[1] < 9:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: f(*args, **kwargs))
    else:
        return await asyncio.to_thread(f, *args, **kwargs)
