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
        return [render(s) for s in source]
    elif isinstance(source, dict):
        return {k: render(v) for k, v in source.items()}
    elif isinstance(source, int):
        return source
    else:
        raise ValueError(f"Invalid template source: {source}")
