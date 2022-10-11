from abc import ABCMeta, abstractmethod
from typing import Optional

from client.alarm_manager import AlarmManager


class Command(metaclass=ABCMeta):
    def __init__(self, command: Optional[str] = None):
        self.command = command
        self.alarm_manager = AlarmManager()

    @property
    @abstractmethod
    def usage(self):
        pass

    @property
    @abstractmethod
    def example(self):
        pass

    @property
    @abstractmethod
    def explanation(self):
        pass

    @abstractmethod
    def is_compatible(self) -> bool:
        pass

    @abstractmethod
    def run(self) -> str:
        pass

    def __str__(self):
        tabs_amount = 7 - (len(self.usage) // 4)
        tabs = tabs_amount * "\t"
        return f"{self.usage}{tabs}{self.explanation} ({self.example})"
