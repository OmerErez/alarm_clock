from datetime import datetime

from cli.commands.command import Command
from cli.consts import DATETIME_FORMAT
from models.alarm import Alarm


class AddCommand(Command):
    @property
    def usage(self):
        return 'add'

    @property
    def example(self):
        return 'add'

    @property
    def explanation(self):
        return 'Add a new alarm'

    def is_compatible(self) -> bool:
        return self.command.lower() == 'add'

    def run(self) -> str:
        alarm_name = input("Enter Alarm Name: ")
        alarm_datetime = input(f"Enter Alarm Datetime (format: {DATETIME_FORMAT}): ")
        alarm_datetime_obj = datetime.strptime(alarm_datetime, DATETIME_FORMAT)
        alarm_obj = Alarm(name=alarm_name, alarm_datetime=alarm_datetime_obj)
        self.alarm_manager.create_alarm(alarm_obj)
        return 'Successfully Created Alarm.'
