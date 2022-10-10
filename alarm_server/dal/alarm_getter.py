from http import HTTPStatus

from fastapi import Response

from adapters.alarm_adapter import AlarmAdapter
from alarm_server.dal.dal_base import DALBase
from alarm_server.dal.queries import GetQueries


class AlarmGetter(DALBase):
    def get_all_alarms(self):
        with self.db_manager as db_manager:
            raw_alarms = db_manager.execute_query(GetQueries.GET_ALL_ALARMS)
        return [AlarmAdapter.adapt_alarm_from_dict(alarm) for alarm in raw_alarms]

    def get_alarm(self, alarm_id: int):
        with self.db_manager as db_manager:
            raw_alarm = db_manager.execute_query(GetQueries.GET_SPECIFIC_ALARM, parameters=[alarm_id], fetch_one=True)
        if raw_alarm is None:
            return Response(status_code=HTTPStatus.NOT_FOUND)
        return AlarmAdapter.adapt_alarm_from_dict(raw_alarm)

    def get_waiting_alarms(self):
        with self.db_manager as db_manager:
            raw_alarms = db_manager.execute_query(GetQueries.GET_WAITING_ALARMS)
        return [AlarmAdapter.adapt_alarm_from_dict(alarm) for alarm in raw_alarms]
