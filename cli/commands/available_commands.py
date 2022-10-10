from cli.commands.add_command import AddCommand
from cli.commands.edit_command import EditCommand
from cli.commands.exit_command import ExitCommand
from cli.commands.get_all_command import GetAllCommand
from cli.commands.get_specific_command import GetSpecificCommand
from cli.commands.remove_command import RemoveCommand

AVAILABLE_COMMANDS = [AddCommand, EditCommand, ExitCommand, GetAllCommand, GetSpecificCommand, RemoveCommand]
