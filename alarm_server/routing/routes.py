from typing import List

from fastapi.routing import APIRoute

from alarm_server.consts import DB_MANAGER
from alarm_server.dal.alarm_creator import AlarmCreator
from alarm_server.dal.alarm_editor import AlarmEditor
from alarm_server.dal.alarm_getter import AlarmGetter
from alarm_server.dal.alarm_remover import AlarmRemover
from alarm_server.routing.router import Router
from models.alarm import Alarm


class AlarmsRouter:
    alarms_getter = AlarmGetter(DB_MANAGER)
    alarms_creator = AlarmCreator(DB_MANAGER)
    alarms_editor = AlarmEditor(DB_MANAGER)
    alarms_remover = AlarmRemover(DB_MANAGER)
    ALARMS = Router(prefix="/alarm", routes=[
        APIRoute(path='', endpoint=alarms_getter.get_all_alarms, methods=['GET'],
                 response_model=List[Alarm]),
        APIRoute(path='/awaiting', endpoint=alarms_getter.get_waiting_alarms, methods=['GET'],
                 response_model=List[Alarm]),
        APIRoute(path='/{alarm_id}', endpoint=alarms_getter.get_alarm, methods=['GET'],
                 response_model=Alarm),
        APIRoute(path='', endpoint=alarms_creator.create_new_alarm, methods=['POST']),
        APIRoute(path='/{alarm_id}', endpoint=alarms_editor.edit_alarm, methods=['PUT']),
        APIRoute(path='/{alarm_id}', endpoint=alarms_remover.remove_alarm, methods=['DELETE'])
    ])


class Routes:
    ROUTERS = [AlarmsRouter.ALARMS]
