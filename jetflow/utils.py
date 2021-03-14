import importlib


def import_string(name):
    names = name.split(':')
    if len(names) != 2:
        raise ImportError(f'{name} is invalid import string.')
    module_name, local_name = names
    module = importlib.import_module(module_name)
    return getattr(module, local_name)
