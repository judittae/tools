# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: ShiftBoard
def reset_demo_data():
    """Возвращает систему в изначальный демо-состояние."""
    global employees, roles, shifts, breaks, swaps, notes, user_id
    employees = [
        {"id": 1, "name": "Алексей", "role": "admin"},
        {"id": 2, "name": "Мария", "role": "employee"},
        {"id": 3, "name": "Дмитрий", "role": "employee"},
        {"id": 4, "name": "Елена", "role": "employee"},
    ]
    roles = ["admin", "manager", "cashier"]
    shifts = [
        {"id": 1, "user_id": 2, "start": "08:00", "end": "20:00", "status": "active"},
        {"id": 2, "user_id": 3, "start": "09:00", "end": "21:00", "status": "active"},
    ]
    breaks = []
    swaps = {}
    notes = {}
    user_id = None

def clear_state():
    """Полностью очищает все данные и сбрасывает пользователя."""
    global employees, roles, shifts, breaks, swaps, notes, user_id
    employees = [
        {"id": 1, "name": "Алексей", "role": "admin"},
    ]
    roles = []
    shifts = []
    breaks = []
    swaps = {}
    notes = {}
    user_id = None
