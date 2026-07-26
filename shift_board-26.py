# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: ShiftBoard
def run_demo():
    print("=== ShiftBoard Demo ===")
    demo = {
        "employees": [
            {"id": 1, "name": "Alice", "role": "engineer"},
            {"id": 2, "name": "Bob", "role": "manager"},
            {"id": 3, "name": "Charlie", "role": "engineer"},
        ],
        "roles": ["engineer", "manager"],
    }
    for emp in demo["employees"]:
        print(f"Employee: {emp['name']} (Role: {emp['role']})")

    shifts = [
        {"employee_id": 1, "date": "2024-06-01", "start": "08:00", "end": "17:00"},
        {"employee_id": 2, "date": "2024-06-01", "start": "09:00", "end": "18:00"},
        {"employee_id": 3, "date": "2024-06-02", "start": "08:00", "end": "17:00"},
    ]
    print(f"\nTotal shifts scheduled: {len(shifts)}")

    notes = [
        {"employee_id": 1, "date": "2024-06-01", "text": "Working from home"},
    ]
    for note in notes:
        print(f"Note: {note['text']} (for {note['employee_id']})")

    swaps = [
        {"employee_id": 1, "date": "2024-06-03", "replacement_id": 3},
    ]
    for swap in swaps:
        print(f"Swap: {swap['employee_id']} replaced by {swap['replacement_id']} on {swap['date']}")

    run_demo()
