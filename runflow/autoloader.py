"""
Auto-load a .hcl file using Python import string.

Say, we have a file `mypackage/my_flow.hcl`,
you can get the flow object by running the statements like below::

    >>> import runflow.autoloader
    >>> from mypackage.my_flow import flow
"""
import os
import sys
from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_loader

from .core import Flow


EXT_RUNFLOW = ".hcl"


# pylint: disable=abstract-method
class FlowLoader(Loader):
    """Load .hcl file.

    See https://docs.python.org/3/library/importlib.html#importlib.abc.Loader
    """

    def __init__(self, full_path):
        self._full_path = full_path
        self._flow = None

    def create_module(self, spec):
        """Load .hcl to a Flow object."""
        try:
            self._flow = Flow.from_specfile(self._full_path)
        except Exception as err:
            raise ImportError from err

    def exec_module(self, module):
        """Execute the flow module when the module is loaded.

        This method assigns variable `flow` to the loaded Flow object.
        """
        module.__dict__.update({"flow": self._flow})


# pylint: disable=no-self-use
class FlowMetaPathFinder(MetaPathFinder):
    """A meta path finder for a .hcl file."""

    def find_spec(self, fullname, path, target=None):
        """Find import-related information used to load a Flow module."""
        mod_name = fullname.split(".")[-1]
        paths = path if path else [os.path.abspath(os.curdir)]
        for check_path in paths:
            full_path = os.path.join(check_path, mod_name + EXT_RUNFLOW)
            if os.path.exists(full_path):
                return spec_from_loader(fullname, FlowLoader(full_path))
        return None


sys.meta_path.insert(0, FlowMetaPathFinder())
