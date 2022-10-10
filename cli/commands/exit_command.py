import sys

from cli.commands.command import Command


class ExitCommand(Command):
    @property
    def usage(self):
        return 'exit'

    @property
    def example(self):
        return 'exit'

    @property
    def explanation(self):
        return 'Exit system'

    def is_compatible(self) -> bool:
        return self.command.lower() == 'exit'

    def run(self):
        sys.exit(0)
