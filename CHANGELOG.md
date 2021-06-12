# Changelog

## Not Yet Released

[Code Changes](https://github.com/soasme/runflow/compare/v0.3.0..HEAD).

## v0.3.0, 12 Jun, 2021

[Code Changes](https://github.com/soasme/runflow/compare/v0.2.0..v0.3.0).

* Unified vars. [#10](https://github.com/soasme/runflow/pull/10)
* New task tyep: `template`.
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
