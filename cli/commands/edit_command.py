from datetime import datetime

import requests

from cli.commands.alarm_id_command import AlarmIDCommand
from cli.consts import DATETIME_FORMAT
from models.alarm import Alarm


class EditCommand(AlarmIDCommand):
    @property
    def usage(self):
        return 'edit {alarm_id}'

    @property
    def example(self):
        return 'edit 1'

    @property
    def explanation(self):
        return 'Edit a specific alarm'

    def is_compatible(self) -> bool:
        return self.command.split()[0].lower() == 'edit' and self.alarm_id.isdigit() and len(self.command.split()) == 2

    @staticmethod
    def _get_new_alarm(original_alarm: Alarm) -> Alarm:
        alarm_name = input("Enter New Alarm Name (Blank to keep): ")
        alarm_datetime = input(f"Enter New Alarm Datetime (format: {DATETIME_FORMAT}) (Blank to keep): ")
        if alarm_name:
            original_alarm.name = alarm_name
        if alarm_datetime:
            alarm_datetime_obj = datetime.strptime(alarm_datetime, DATETIME_FORMAT)
            original_alarm.alarm_datetime = alarm_datetime_obj
        return original_alarm

    def run(self) -> str:
        try:
            original_alarm = self.alarm_manager.get_specific_alarm(self.alarm_id)
            new_alarm = self._get_new_alarm(original_alarm)
            self.alarm_manager.edit_alarm(self.alarm_id, new_alarm)
            return 'Successfully Edited Alarm.'
        except requests.exceptions.HTTPError:
            return 'Non Existent!'
