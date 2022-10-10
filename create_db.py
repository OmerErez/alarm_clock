from alarm_server.consts import DB_FILE_NAME
from alarm_server.db_manager.db_manager import DBManager

if __name__ == '__main__':
    if input("Are you sure? (enter Y): ") == 'Y':
        with DBManager(DB_FILE_NAME) as db_manager:
            db_manager.execute_query("""
                CREATE TABLE "Alarms" (
            "id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT NOT NULL,
            "alarm_datetime"	datetime NOT NULL,
            "triggered"	REAL NOT NULL DEFAULT 0,
            PRIMARY KEY("id")
        )
            """, commit=True)
