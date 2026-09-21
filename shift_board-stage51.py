# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: ShiftBoard
class AuditLog:
    def __init__(self):
        self._records = []

    def log(self, action: str, entity: str, details: dict, user: str):
        self._records.append({
            "time": datetime.now().isoformat(),
            "action": action,
            "entity": entity,
            "details": details,
            "user": user,
        })
        return self._records[-1]

    def get(self) -> list:
        return list(self._records)

    def clear(self):
        self._records.clear()
