from abc import ABC

from cli.commands.command import Command


class AlarmIDCommand(Command, ABC):
    @property
    def alarm_id(self):
        try:
            return self.command.split()[1]
        except IndexError:
            raise Exception(f'Usage: {self.example}')
