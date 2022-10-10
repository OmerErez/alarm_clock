from http import HTTPStatus

from fastapi import Response

from alarm_server.dal.dal_base import DALBase
from alarm_server.dal.queries import DeleteQueries


class AlarmRemover(DALBase):
    def remove_alarm(self, alarm_id: int):
        with self.db_manager as db_manager:
            affected_rows = db_manager.execute_query(DeleteQueries.DELETE_ALARM, parameters=[alarm_id], commit=True)
            if affected_rows == 0:
                return Response(status_code=HTTPStatus.NOT_FOUND)
