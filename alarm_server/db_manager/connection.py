import sqlite3
from typing import Optional


class Connection:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor: Optional[sqlite3.Cursor] = None

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
