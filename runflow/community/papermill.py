"""
This module wraps `papermill` library as a task type.
"""

from pathlib import Path
from typing import Union, Optional

import attr


@attr.s(
    auto_attribs=True,
    kw_only=True,
    frozen=True,
)
class PapermillExecuteTask:
    """This class implements task type `papermill_exuecte`."""

    input_path: Union[str, Path] = attr.ib(
        validator=attr.validators.instance_of((str, Path)),
    )
    output_path: Union[str, Path] = attr.ib(
        validator=attr.validators.instance_of((str, Path)),
    )
    parameters: dict = attr.ib(
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )
    engine_name: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)),
        default=None,
    )
    request_save_on_cell_execute: bool = attr.ib(
        validator=attr.validators.instance_of(bool),
        default=True,
    )
    prepare_only: bool = attr.ib(
        validator=attr.validators.instance_of(bool),
        default=False,
    )
    kernel_name: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)),
        default=None,
    )
    language: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)),
        default=None,
    )
    progress_bar: bool = attr.ib(
        validator=attr.validators.instance_of(bool),
        default=True,
    )
    log_output: bool = attr.ib(
        validator=attr.validators.instance_of(bool),
        default=False,
    )
    stdout_file: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)),
        default=None,
    )
    stderr_file: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)),
        default=None,
    )
    start_timeout: int = attr.ib(
        validator=attr.validators.instance_of((int, float)),
        default=60,
    )
    report_mode: bool = attr.ib(
        validator=attr.validators.instance_of(bool),
        default=False,
    )
    cwd: Optional[Union[str, Path]] = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of((str, Path))
        ),
        default=None,
    )
    engine_config: dict = attr.ib(
        validator=attr.validators.instance_of(dict),
        factory=dict,
    )

    def run(self):
        try:
            from papermill import execute_notebook
        except ImportError as err:
            raise ImportError("Please install runflow[papermill]") from err

        notebook = execute_notebook(
            input_path=self.input_path,
            output_path=self.output_path,
            parameters=self.parameters,
            engine_name=self.engine_name,
            request_save_on_cell_execute=self.request_save_on_cell_execute,
            prepare_only=self.prepare_only,
            kernel_name=self.kernel_name,
            language=self.language,
            progress_bar=self.progress_bar,
            log_output=self.log_output,
            stdout_file=self.stdout_file,
            stderr_file=self.stderr_file,
            start_timeout=self.start_timeout,
            report_mode=self.report_mode,
            cwd=self.cwd,
            **self.engine_config,
        )
        return {"notebook": notebook}
