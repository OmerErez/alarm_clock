from alarm_server.consts import DB_MANAGER

if __name__ == '__main__':
    if input("Are you sure? (enter Y): ") == 'Y':
        with DB_MANAGER as db_manager:
            db_manager.execute_query("""
                CREATE TABLE "Alarms" (
            "id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT NOT NULL,
            "alarm_datetime"	datetime NOT NULL,
            "triggered"	REAL NOT NULL DEFAULT 0,
            PRIMARY KEY("id")
        )
            """, commit=True)
