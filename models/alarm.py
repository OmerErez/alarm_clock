from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Alarm(BaseModel):
    id: Optional[int] = None
    name: str
    alarm_datetime: datetime
    triggered: bool = False

    def to_dict(self):
        return dict(id=self.id, name=self.name, triggered=self.triggered,
                    alarm_datetime=self.alarm_datetime.isoformat())

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, alarm time: {self.alarm_datetime}, triggered: {self.triggered}'
