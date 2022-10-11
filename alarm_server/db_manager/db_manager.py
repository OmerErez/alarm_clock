import sqlite3
from typing import Optional, Any, Iterable

from alarm_server.db_manager.connection import Connection


class DBManager:
    def __init__(self, db_file_name: str):
        self.db_file_name = db_file_name
        self.connection: Optional[sqlite3.Connection] = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_file_name, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row

    def disconnect(self):
        self.connection.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def execute_query(self, query: str, parameters: Optional[Iterable[Any]] = (), commit: bool = False,
                      fetch_one: bool = False):
        with Connection(self.connection) as cursor:
            cursor.execute(query, parameters)
            if not commit:
                if fetch_one:
                    return cursor.fetchone()
                return cursor.fetchall()
            self.connection.commit()
            return cursor.rowcount
