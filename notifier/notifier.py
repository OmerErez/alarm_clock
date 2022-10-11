import ctypes
import time

from client.alarm_manager import AlarmManager
from models.alarm import Alarm


class Notifier:
    def __init__(self):
        self.alarm_manager = AlarmManager()

    def alarm(self, alarm: Alarm):
        alarm.triggered = True
        self.alarm_manager.edit_alarm(alarm.id, alarm)
        ctypes.windll.user32.MessageBoxW(0, alarm.name, 'New Alarm!', 0x1000)

    def start(self):
        while True:
            awaiting_alarms = self.alarm_manager.get_all_awaiting_alarms()
            if len(awaiting_alarms):
                for alarm in awaiting_alarms:
                    self.alarm(alarm)
            time.sleep(1)
