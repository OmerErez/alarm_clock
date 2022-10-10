from adapters.alarm_adapter import AlarmAdapter
from models.alarm import Alarm
from client.server_communicator import ServerCommunicator
from client.consts import BASE_URL


class AlarmManager:
    def __init__(self):
        self.server_communicator = ServerCommunicator(BASE_URL)

    def get_all_alarms(self):
        response = self.server_communicator.get("")
        response.raise_for_status()
        return [AlarmAdapter.adapt_alarm_from_dict(alarm) for alarm in response.json()]

    def get_specific_alarm(self, alarm_id: int):
        response = self.server_communicator.get(str(alarm_id))
        response.raise_for_status()
        return AlarmAdapter.adapt_alarm_from_dict(response.json())

    def get_all_awaiting_alarms(self):
        response = self.server_communicator.get("awaiting")
        response.raise_for_status()
        return [AlarmAdapter.adapt_alarm_from_dict(alarm) for alarm in response.json()]

    def create_alarm(self, alarm: Alarm):
        response = self.server_communicator.post("", alarm.to_dict())
        response.raise_for_status()

    def edit_alarm(self, alarm_id: int, alarm: Alarm):
        response = self.server_communicator.put(str(alarm_id), alarm.to_dict())
        response.raise_for_status()

    def remove_alarm(self, alarm_id: int):
        response = self.server_communicator.delete(str(alarm_id))
        response.raise_for_status()
