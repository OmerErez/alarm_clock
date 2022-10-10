from alarm_server.dal.dal_base import DALBase
from alarm_server.dal.queries import InsertQueries
from models.alarm import Alarm


class AlarmCreator(DALBase):
    def create_new_alarm(self, alarm: Alarm):
        with self.db_manager as db_manager:
            return db_manager.execute_query(InsertQueries.CREATE_ALARM,
                                            parameters=[alarm.name, alarm.alarm_datetime, alarm.triggered], commit=True)
