import sqlite3

from runflow.utils import to_thread

class Sqlite3ExecTask:

    def __init__(self, sql, parameters=None, dsn=':memory:', autocommit=True, exec_many=False):
        self.dsn = dsn
        self.sql = sql
        self.parameters = parameters or []
        self.autocommit = autocommit
        self.exec_many = exec_many

    def sync_run(self, context):
        with sqlite3.connect(self.dsn) as conn:
            cursor = conn.cursor()
            if not self.parameters:
                cursor.execute(self.sql)
            elif self.exec_many:
                cursor.executemany(self.sql, self.parameters)
            else:
                cursor.execute(self.sql, self.parameters)

            rowcount = cursor.rowcount

            if self.autocommit:
                conn.commit()

            return {'rowcount': rowcount}

    async def run(self, context):
        return await to_thread(self.sync_run, context)

class Sqlite3RowTask:

    def __init__(self, sql, parameters=None, dsn=':memory:', exec_many=True):
        self.dsn = dsn
        self.sql = sql
        self.parameters = parameters or []
        self.exec_many = exec_many

    def sync_run(self, context):
        with sqlite3.connect(self.dsn) as conn:
            cursor = conn.cursor()
            if self.parameters:
                cursor.execute(self.sql, self.parameters)
            else:
                cursor.execute(self.sql)

            if self.exec_many:
                rows = cursor.fetchall()
                return {'rows': rows}
            else:
                row = cursor.fetchone()
                return {'rows': [row]}

    async def run(self, context):
        return await to_thread(self.sync_run, context)
