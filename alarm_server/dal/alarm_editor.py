from http import HTTPStatus

from alarm_server.dal.dal_base import DALBase
from alarm_server.dal.queries import UpdateQueries
from models.alarm import Alarm
from fastapi import Response


class AlarmEditor(DALBase):
    def edit_alarm(self, alarm_id: int, alarm: Alarm):
        with self.db_manager as db_manager:
            affected_rows = db_manager.execute_query(UpdateQueries.UPDATE_ALARM,
                                                     parameters=[alarm.name, alarm.alarm_datetime, alarm.triggered,
                                                                 alarm_id],
                                                     commit=True)
            if affected_rows == 0:
                return Response(status_code=HTTPStatus.NOT_FOUND)
