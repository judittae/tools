# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: ShiftBoard
def find_duplicate(boards, new_record, record_type):
    for board in boards:
        if board.get("id") != new_record.get("id"):
            same_type = any(
                r.get("type") == record_type
                and r.get("board_id") == board.get("id")
                and r.get("date") == new_record.get("date")
                and r.get("employee_id") == new_record.get("employee_id")
                and r.get("start_time") == new_record.get("start_time")
                and r.get("end_time") == new_record.get("end_time")
                for r in board.get("records", [])
            )
            if same_type:
                return f"Запись уже существует в смене {board.get('name')}"
    return None

def check_duplicate_shifts(boards, new_shift, employee_id, start_time, end_time):
    for board in boards:
        for record in board.get("records", []):
            if record.get("employee_id") == employee_id and record.get("start_time") == start_time and record.get("end_time") == end_time:
                return f"Смена уже запланирована для {record.get('employee_name')}"
    return None

def check_duplicate_notes(boards, new_note, employee_id, shift_id):
    for board in boards:
        for record in board.get("records", []):
            if record.get("id") == shift_id:
                for note in record.get("notes", []):
                    if note.get("employee_id") == employee_id:
                        return f"Заметка уже добавлена для {note.get('employee_name')}"
    return None

def check_duplicate_swaps(boards, new_swap, employee_id, shift_id):
    for board in boards:
        for record in board.get("records", []):
            if record.get("id") == shift_id:
                for swap in record.get("swaps", []):
                    if swap.get("employee_id") == employee_id:
                        return f"Замена уже предложена для {swap.get('employee_name')}"
    return None
