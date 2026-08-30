# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: ShiftBoard
def repair_data():
    """Простая проверка целостности и ремонт типовых проблем."""
    repaired = 0
    for i in range(len(employees)):
        if not isinstance(employees[i], dict) or 'name' not in employees[i]:
            employees[i] = {'name': f'Unknown Worker {i}', 'role': None, 'schedule': []}
            repaired += 1
    for i in range(len(shifts)):
        if not isinstance(shifts[i], dict) or 'employee' not in shifts[i] or 'start' not in shifts[i] or 'end' not in shifts[i]:
            shifts[i] = {'employee': None, 'start': None, 'end': None, 'role': None, 'notes': '', 'replaced_by': None, 'replaced_at': None}
            repaired += 1
    return repaired
