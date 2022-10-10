from alarm_server.db_manager.db_manager import DBManager


class DALBase:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager
