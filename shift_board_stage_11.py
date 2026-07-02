# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: ShiftBoard
import json, os

def save_to_file(data: dict, path: str = "shiftboard.json") -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_file(path: str = "shiftboard.json") -> dict:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Ошибка чтения файла конфигурации.")
        return {}

def get_default_data() -> dict:
    return {
        "employees": [],
        "roles": [],
        "shifts": [],
        "notes": []
    }
