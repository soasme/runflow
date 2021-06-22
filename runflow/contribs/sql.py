from sqlalchemy import create_engine, text


class SqlExecTask:

    def __init__(self, dsn, sql, parameters=None, autocommit=True):
        self.engine = create_engine(str(dsn), echo=False, future=True)
        self.sqls = sql
        self.parameters = parameters or []
        self.autocommit = autocommit

    def run(self, context):
        with self.engine.begin() as conn:
            conn = conn.execution_options(autocommit=self.autocommit)
            for sql in self.sqls:
                statement = text(sql['statement'])
                parameters = sql.get('parameters') or None
                conn.execute(statement, parameters)
        return {}


class SqlRowTask:

    def __init__(self, dsn, sql, parameters=None):
        self.engine = create_engine(str(dsn), echo=False, future=True)

        if len(sql) != 1:
            raise ValueError('sql_row supports only one sql block.')

        self.sql = sql[0]
        self.parameters = parameters or []

    def run(self, context):
        with self.engine.begin() as conn:
            statement = text(self.sql['statement'])
            parameters = self.sql.get('parameters') or None
            result = conn.execute(statement, parameters)
            rows = [dict(m) for m in result.mappings()]
            return {'rows': rows}
