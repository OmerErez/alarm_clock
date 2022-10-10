from copy import deepcopy

from cli.commands.available_commands import AVAILABLE_COMMANDS
from cli.commands.help_command import HelpCommand


class CommandLineInterface:
    def __init__(self):
        print("Welcome to alarm command line interface.")
        print(HelpCommand().run())

    @property
    def available_commands(self):
        available_commands = deepcopy(AVAILABLE_COMMANDS)
        available_commands.append(HelpCommand)
        return available_commands

    def run_command(self, command: str):
        for command_type in self.available_commands:
            command_obj = command_type(command)
            if command_obj.is_compatible():
                return command_obj.run()
        return 'Command Not Found.'

    def start(self):
        while True:
            command = input(">>> ")
            try:
                print(self.run_command(command))
            except IndexError:
                print("Command Not Found.")
            except Exception as e:
                print(e)


if __name__ == '__main__':
    CommandLineInterface().start()
