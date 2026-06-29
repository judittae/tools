# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: ShiftBoard
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        required_keys = ["employees", "roles", "shifts", "notes"]
        missing = [k for k in required_keys if k not in data]
        if missing:
            raise KeyError(f"Отсутствуют ключи: {', '.join(missing)}")
            
        # Валидация типов данных для основных сущностей
        if not isinstance(data["employees"], list):
            raise TypeError("Сотрудники должны быть списком")
        
        for emp in data["employees"]:
            if not all(isinstance(emp.get(k), (str, int)) for k in ["id", "name", "role_id"]):
                raise ValueError(f"Некорректая запись сотрудника: {emp}")

        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка валидации данных: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (раскомментируйте при запуске):
if __name__ == "__main__":
    # Замените эту строку на вашу JSON-строку или путь к файлу
    json_data = '{"employees":[{"id":1,"name":"Иван","role_id":2}],"roles":[],"shifts":[],"notes":[]}' 
    initial_state = load_initial_data(json_data)
    print(f"Загружено {len(initial_state['employees'])} сотрудников")
