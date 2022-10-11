import requests

from cli.commands.alarm_id_command import AlarmIDCommand


class GetSpecificCommand(AlarmIDCommand):
    @property
    def usage(self):
        return 'get {alarm_id}'

    @property
    def example(self):
        return 'get 1'

    @property
    def explanation(self):
        return 'Get a specific alarm'

    def is_compatible(self) -> bool:
        return self.command.split()[0].lower() == 'get' and self.alarm_id.isdigit() and len(self.command.split()) == 2

    def run(self) -> str:
        try:
            return self.alarm_manager.get_specific_alarm(self.alarm_id)
        except requests.exceptions.HTTPError:
            return 'Non Existent!'
