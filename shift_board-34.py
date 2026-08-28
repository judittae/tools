# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: ShiftBoard
TEMPLATES = {
    "morning_shift": {"role": "morning", "hours": 8, "start": 7, "end": 15},
    "evening_shift": {"role": "evening", "hours": 8, "start": 15, "end": 23},
    "night_shift": {"role": "night", "hours": 12, "start": 21, "end": 9},
    "lunch": {"role": "lunch", "hours": 1, "start": 12, "end": 13},
    "breakfast": {"role": "breakfast", "hours": 1, "start": 7, "end": 8},
    "dinner": {"role": "dinner", "hours": 1, "start": 19, "end": 20},
}

def apply_template(template_name, record):
    if template_name not in TEMPLATES:
        raise ValueError(f"Unknown template: {template_name}")
    t = TEMPLATES[template_name]
    record["role"] = t["role"]
    record["hours"] = t["hours"]
    record["start"] = t["start"]
    record["end"] = t["end"]
    return record
