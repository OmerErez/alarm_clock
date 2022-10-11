from copy import deepcopy

from cli.commands.available_commands import AVAILABLE_COMMANDS
from cli.commands.command import Command


class HelpCommand(Command):
    @property
    def usage(self):
        return 'help'

    @property
    def example(self):
        return 'help'

    @property
    def explanation(self):
        return 'Show help message'

    def is_compatible(self) -> bool:
        return self.command.lower() == 'help'

    def run(self):
        available_commands = deepcopy(AVAILABLE_COMMANDS)
        available_commands.append(HelpCommand)
        return "\n".join(str(command()) for command in available_commands)
