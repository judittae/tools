# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: ShiftBoard
import datetime
from dataclasses import dataclass, field
from typing import List


@dataclass
class Reminder:
    target_name: str
    message: str
    due_date: datetime.date = None
    is_done: bool = False
    notes: str = ""
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    def __post_init__(self):
        if self.due_date is None:
            today = datetime.date.today()
            self.due_date = today


@dataclass
class ReminderManager:
    reminders: List[Reminder] = field(default_factory=list)

    def add(self, target_name: str, message: str, due_date=None):
        rem = Reminder(target_name=target_name, message=message, due_date=due_date)
        self.reminders.append(rem)
        return rem

    def get_overdue(self) -> List[Reminder]:
        today = datetime.date.today()
        return [r for r in self.reminders if not r.is_done and (r.due_date - today).days < 0]

    def mark_done(self, target_name: str):
        for i, rem in enumerate(self.reminders):
            if rem.target_name == target_name and not rem.is_done:
                rem.is_done = True
                return rem
        raise ValueError(f"No undone reminder found for {target_name}")

    def get_upcoming(self, days=7) -> List[Reminder]:
        today = datetime.date.today()
        cutoff = today + datetime.timedelta(days=days)
        return [r for r in self.reminders if not r.is_done and r.due_date <= cutoff]

    def list_all(self):
        return self.reminders
