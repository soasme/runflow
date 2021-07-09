from typing import List, Optional, Union

import attr
from sqlalchemy import create_engine, text


@attr.s(
    auto_attribs=True,
    kw_only=True,
    frozen=True,
)
class SqlExecTask:
    """This task execute sql statement on a sql database."""

    dsn: str = attr.ib(validator=attr.validators.instance_of(str))
    sql: List[str] = attr.ib(validator=attr.validators.instance_of(list))
    parameters: Optional[Union[dict, list]] = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of((dict, list))
        ),
        default=None,
    )
    autocommit: bool = True

    # pylint: disable=no-self-use
    @sql.validator
    def _check_sql_statement(self, field, value):
        for sql in value:
            if not isinstance(sql, dict) or "statement" not in sql:
                raise ValueError("invalid sql: no sql.statement")

    def run(self):
        engine = create_engine(str(self.dsn), echo=False, future=True)
        with engine.begin() as conn:
            conn = conn.execution_options(autocommit=self.autocommit)
            for sql in self.sql:
                statement = text(sql["statement"])
                parameters = sql.get("parameters") or None
                conn.execute(statement, parameters)
        return {}


@attr.s(
    auto_attribs=True,
    kw_only=True,
    frozen=True,
)
class SqlRowTask:
    """This task fetch data from a sql database."""

    dsn: str = attr.ib(validator=attr.validators.instance_of(str))
    sql: List[str] = attr.ib(validator=attr.validators.instance_of(list))
    parameters: Optional[Union[dict, list]] = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of((dict, list))
        ),
        default=None,
    )

    # pylint: disable=no-self-use
    @sql.validator
    def _check_sql_statement(self, field, value):
        if len(value) != 1:
            raise ValueError("invalid sql: require one sql block")

        sql = value[0]
        if not isinstance(sql, dict) or "statement" not in sql:
            raise ValueError("invalid sql: no sql.statement")

    def run(self):
        engine = create_engine(str(self.dsn), echo=False, future=True)
        with engine.begin() as conn:
            statement = text(self.sql[0]["statement"])
            parameters = self.sql[0].get("parameters") or None
            result = conn.execute(statement, parameters)
            rows = [dict(m) for m in result.mappings()]
            return {"rows": rows}
