# Changelog

## Not Yet Released

[Code Changes](https://github.com/soasme/runflow/compare/v0.8.1..HEAD).

## v0.9.0, 8 Jul, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.8.1..v0.9.0).

* Bugfix: `_retry` not working for `tenacity>=8.0.0`. [#60](https://github.com/soasme/runflow/pull/60).
* New Task Type: `telegram_api_call`. [#61](https://github.com/soasme/runflow/pull/61).
* New Task Type: `feed_parse`. [#60](https://github.com/soasme/runflow/pull/60).
* New Task Type: `pushbullet_push`. [#59](https://github.com/soasme/runflow/pull/59).
* New Task Type: `smtp_send`. [#58](https://github.com/soasme/runflow/pull/58).
* Enhancement: Support installing all extras packages via `runflow[all]`. [#59](https://github.com/soasme/runflow/pull/59).
* Tutorial: [Use Scikit-Learn and Runflow](https://runflow.org/tutorials/sklearn-and-runflow.html).

## v0.8.1, 6 Jul, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.8.0..v0.8.1).

* Code Quality: Add type hints and mypy check. [#56](https://github.com/soasme/runflow/pull/56).
* New Task Type: `slack_api_call`. [#55](https://github.com/soasme/runflow/pull/55).
* Documentation: <https://runflow.org/concepts.html>. [#54](https://github.com/soasme/runflow/pull/54).
* Enhancement: Add upstream task reference if the task is a FlowRunTask. [#53](https://github.com/soasme/runflow/pull/53).
* Enhancement: Support import a flow as a new task type. [#52](https://github.com/soasme/runflow/pull/52).
* Enhancement: Support `_timeout` for all task types. [#51](https://github.com/soasme/runflow/pull/51).
* Bugfix: The direction of flow graph direction is wrong. [#50](https://github.com/soasme/runflow/pull/50).
* Enhancement: Remove parameter `context` from Task.run. [#49](https://github.com/soasme/runflow/pull/49).
* Bugfix: Can't detect implicit task dependency in hcl2 call syntax. [#48](https://github.com/soasme/runflow/pull/48).

## v0.8.0, 2 Jul, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.7.0..v0.8.0).

* Enhancement: HCL parser support star args and double-star args using `...`. [#47](https://github.com/soasme/runflow/pull/47).
* Enhancement: New argument `b64content` for task type `file_write`. [#46](https://github.com/soasme/runflow/pull/46).
* Enhancement: New option `--var-file` for command `runflow run`. [#45](https://github.com/soasme/runflow/pull/45).
* Enhancement: New command: `runflow visualize`. [#44](https://github.com/soasme/runflow/pull/44).

## v0.7.0, 2 Jul, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.6.0..v0.7.0).

* Enhancement: Support `_retry` for all tasks. [#41](https://github.com/soasme/runflow/pull/41), [#43](https://github.com/soasme/runflow/pull/43).
* Enhancement: Task `flow_run` can now export variables through `export` blocks. [#36](https://github.com/soasme/runflow/pull/36), [#42](https://github.com/soasme/runflow/pull/42).
* Enhancement: Task private arguments are now starting with an underscore `_`. [#37](https://github.com/soasme/runflow/pull/37).
* Enhancement: Task can now keep running if all of its upstream are successful. [#38](https://github.com/soasme/runflow/pull/38).

## v0.6.0, 24 Jun, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.5.1..v0.6.0).

* Enhancement: `import` block now supports setting the task names and function names. Please check the updated [documentation](https://runflow.org/extend-runflow.html). [#35](https://github.com/soasme/runflow/pull/35).
* Performance Enhancement: use lark standalone parser. [#34](https://github.com/soasme/runflow/pull/34).


## v0.5.1, 23 Jun, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.5.0..v0.5.1).

* Code Quality: Auto-format code via black. [#33](https://github.com/soasme/runflow/pull/33).
* Code Quality: Passed pylint & flake8 checks. [#28](https://github.com/soasme/runflow/pull/28), [#32](https://github.com/soasme/runflow/pull/32).
* Code Quality: Removed all circular imports. [#31](https://github.com/soasme/runflow/pull/31).
* Documentation: Added argument reference to all task types. [#30](https://github.com/soasme/runflow/pull/30).
* Enhancement: Task `file_read` & `file_write` can now read file from local, FTP, zip, Git, GitHub. [#29](https://github.com/soasme/runflow/pull/29).

## v0.5.0, 21 Jun, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.4.4..v0.5.0).

* New task type: `sql_row`. [#26](https://github.com/soasme/runflow/pull/26).
* New task type: `sql_exec`. [#26](https://github.com/soasme/runflow/pull/26).
* Deprecate task type: `sqlte3_exec`. [#26](https://github.com/soasme/runflow/pull/26).
* Deprecate task type: `sqlte3_exec`. [#26](https://github.com/soasme/runflow/pull/26).
* Support `Task.run()` as synchronous method. [#25](https://github.com/soasme/runflow/pull/25).

## v0.4.4, 21 Jun, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.4.2..v0.4.4).

* Built-In function: `call()`. [#24](https://github.com/soasme/runflow/pull/24).
* Built-In function: `datetime()` & `todatetime()`. [#23](https://github.com/soasme/runflow/pull/23).
* Docs: [integrate with apscheduler](https://runflow.org/integrations/apscheduler.html).
* Docs: [built-in functions](https://runflow.org/builtin-functions.html).
* New task type: `flow_run`. [#21](https://github.com/soasme/runflow/pull/21).
* Enhancement: Task `file_write` supports writing to `/dev/stdout`. [#20](https://github.com/soasme/runflow/pull/20).
* Python API: `runflow()` supports loading from path, module, source, or a Flow object. [#19](https://github.com/soasme/runflow/pull/19).

## v0.4.2, 17 Jun, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.3.0..v0.4.2).

* Added Runflow Specification. [#18](https://github.com/soasme/runflow/pull/18).
* Rewrote HCL2 parse & eval engine. [#16](https://github.com/soasme/runflow/pull/16), [#17](https://github.com/soasme/runflow/pull/17).
* New task type: `hcl2_template` (previous know as `template`).
* New task type: `bash_run` (previous known as `command`). [#15](https://github.com/soasme/runflow/pull/15).
* New block type: `import`. [#14](https://github.com/soasme/runflow/pull/14), [#17](https://github.com/soasme/runflow/pull/17).
* Load envvar `RUNFLOW_VAR_xxx` for `variable "xxx"`. [#13](https://github.com/soasme/runflow/pull/13).
* New task type: `sqlite3_row`. [#12](https://github.com/soasme/runflow/pull/12).
* New task type: `sqlite3_exec`. [#12](https://github.com/soasme/runflow/pull/12).
* New task type: `http_request`. [#11](https://github.com/soasme/runflow/pull/11).

## v0.3.0, 12 Jun, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.2.0..v0.3.0).

* Unified vars. [#10](https://github.com/soasme/runflow/pull/10)
* New task type: `template`.
* New task type: `file_write`. [#9](https://github.com/soasme/runflow/pull/9).
* New task type: `file_read`. [#9](https://github.com/soasme/runflow/pull/9).
* New task type: `docker_run`. [#8](https://github.com/soasme/runflow/pull/8).
* Load hcl files via magic `runflow.autoloader`. [#7](https://github.com/soasme/runflow/pull/7).

## v0.2.0, 7 Jun, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.1.0..v0.2.0).

* Command Task now supports setting `env`.
* Task explicit & implicit dependency.
* Detect acyclic task dependency and abort from running.
* Added entry point: `runflow`.
* Drop Python 3.6 support.
* Added GitHub Actions: unit-testing, auto-packaging.

## v0.1.0, 6 Jun, 2021

Yay! Runflow is now open sourced and released with its first version.

Check the docs site: <https://runflow.org>
