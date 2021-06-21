from sqlalchemy import create_engine, text

from runflow.utils import to_thread

class SqlExecTask:

    def __init__(self, dsn, sql, parameters=None, autocommit=True, exec_many=False):
        self.engine = create_engine(str(dsn), echo=False, future=True)
        self.sqls = sql
        self.parameters = parameters or []
        self.autocommit = autocommit
        self.exec_many = exec_many

    def run(self, context):
        with self.engine.begin() as conn:
            for sql in self.sqls:
                if sql.get('parameters'):
                    result = conn.execute(text(sql['statement']), sql['parameters'])
                else:
                    result = conn.execute(text(sql['statement']))
        return {}

class SqlRowTask:

    def __init__(self, dsn, sql, parameters=None, exec_many=True):
        self.engine = create_engine(str(dsn), echo=False, future=True)

        if len(sql) != 1:
            raise ValueError('sql_row supports only one sql block.')

        self.sql = sql[0]
        self.parameters = parameters or []
        self.exec_many = exec_many

    def run(self, context):
        with self.engine.begin() as conn:
            if self.sql.get('parameters'):
                result = conn.execute(text(self.sql['statement']), self.sql['parameters'])
            else:
                result = conn.execute(text(self.sql['statement']))
            rows = [dict(m) for m in result.mappings()]
            return {'rows': rows}
