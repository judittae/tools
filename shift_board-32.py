# === Stage 32: Добавь журнал действий пользователя ===
# Project: ShiftBoard
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action, details=None):
        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "details": details
        }
        self.entries.append(entry)
        return entry
