from typing import Any, Dict

from models.alarm import Alarm


class AlarmAdapter:
    @staticmethod
    def adapt_alarm_from_dict(alarm_dict: Dict[str, Any]) -> Alarm:
        return Alarm(**alarm_dict)
