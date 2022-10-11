from cli.commands.command import Command


class GetAllCommand(Command):
    @property
    def usage(self):
        return 'get'

    @property
    def example(self):
        return 'get'

    @property
    def explanation(self):
        return 'Get all alarms'

    def is_compatible(self) -> bool:
        return self.command.lower() == 'get'

    def run(self) -> str:
        return "\n".join(str(alarm) for alarm in self.alarm_manager.get_all_alarms())
