import sys
import os
from importlib.abc import MetaPathFinder, Loader
from importlib.util import spec_from_loader

from .core import Flow


EXT_RUNFLOW = '.hcl'


__all__ = []


class FlowLoader(Loader):
    def __init__(self, full_path):
        self._full_path = full_path

    def create_module(self, spec):
        try:
            self._flow = Flow.from_specfile(self._full_path)
        except Exception as e:
            raise ImportError from e
        return None

    def exec_module(self, module):
        module.__dict__.update({"flow": self._flow})
        return None


class FlowMetaPathFinder(MetaPathFinder):

    def find_spec(self, fullname, path, target=None):
        mod_name = fullname.split('.')[-1]
        paths = path if path else [os.path.abspath(os.curdir)]
        for check_path in paths:
            full_path = os.path.join(check_path, mod_name + EXT_RUNFLOW)
            if os.path.exists(full_path):
                return spec_from_loader(fullname, FlowLoader(full_path))
        return None


sys.meta_path.insert(0, FlowMetaPathFinder())
