# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: ShiftBoard
def export_to_json():
    import json
    data = {
        "employees": employees,
        "roles": roles,
        "shifts": shifts,
        "notes": notes,
        "swaps": swaps
    }
    return json.dumps(data, indent=2)
