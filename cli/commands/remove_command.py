import requests

from cli.commands.alarm_id_command import AlarmIDCommand


class RemoveCommand(AlarmIDCommand):
    @property
    def usage(self):
        return 'remove {alarm_id}'

    @property
    def example(self):
        return 'remove 1'

    @property
    def explanation(self):
        return 'Remove a specific alarm'

    def is_compatible(self) -> bool:
        return self.command.split()[0].lower() == 'remove' and self.alarm_id.isdigit() and \
               len(self.command.split()) == 2

    def run(self) -> str:
        try:
            self.alarm_manager.remove_alarm(self.alarm_id)
            return 'Successfully Removed Alarm.'
        except requests.exceptions.HTTPError:
            return 'Non Existent!'
