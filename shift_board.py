# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: ShiftBoard
import json, os
from dataclasses import asdict, field
from typing import List, Dict, Any

DATA_DIR = "data"
DB_FILE = os.path.join(DATA_DIR, "shiftboard.json")

def ensure_db():
    if not os.path.exists(DB_FILE):
        os.makedirs(DATA_DIR)
        db: Dict[str, Any] = {
            "employees": [
                {"id": 1, "name": "Алексей", "role": "Врач"},
                {"id": 2, "name": "Мария", "role": "Сестра"}
            ],
            "shifts": [],
            "notes": []
        }
        with open(DB_FILE, "w") as f:
            json.dump(db, f)

def get_db() -> Dict[str, Any]:
    ensure_db()
    with open(DB_FILE, "r") as f:
        return json.load(f)
