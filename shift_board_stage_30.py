# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: ShiftBoard
class UserProfile:
    def __init__(self, name, role, shifts=None):
        self.name = name
        self.role = role
        self.shifts = shifts or {}

    def to_dict(self):
        return {"name": self.name, "role": self.role, "shifts": self.shifts}

    @staticmethod
    def from_dict(data):
        return UserProfile(data["name"], data["role"], data.get("shifts", {}))


def add_user_profiles(db_store):
    profiles = db_store.get("user_profiles", [])
    if not profiles:
        profiles.append(UserProfile("admin", "manager"))
    for p in profiles:
        db_store.setdefault("user_profiles", []).append(p)
