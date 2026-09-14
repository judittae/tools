# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: ShiftBoard
def migrate_shift_data(old_format):
    """Upgrade legacy shift data to current schema.
    Returns updated dict with new keys if old_format is detected."""
    if isinstance(old_format, dict):
        if "shifts" in old_format and old_format["shifts"].get("version", 1) < 2:
            return {
                "version": 2,
                "shifts": {
                    "version": 2,
                    "data": old_format["shifts"]["data"] if "data" in old_format["shifts"] else old_format["shifts"]
                },
                "employees": old_format.get("employees", {}),
                "roles": old_format.get("roles", {}),
                "notes": old_format.get("notes", {}),
            }
    return old_format
