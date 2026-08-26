# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: ShiftBoard
def undo_last():
    if not actions_log:
        print("Нет действий для отката.")
        return
    action = actions_log.pop()
    print(f"Откат: {action['type']}")
    if action['type'] == 'add_shift':
        del shifts[action['shift_id']]
    elif action['type'] == 'update_shift':
        shifts[action['shift_id']] = action['old_shift']
    elif action['type'] == 'delete_shift':
        shifts[action['shift_id']] = action['deleted_shift']
    elif action['type'] == 'add_employee':
        employees[action['emp_id']] = action['old_employee']
    elif action['type'] == 'update_employee':
        employees[action['emp_id']] = action['old_employee']
    elif action['type'] == 'delete_employee':
        employees[action['emp_id']] = action['deleted_employee']
    elif action['type'] == 'add_role':
        roles[action['role_id']] = action['old_role']
    elif action['type'] == 'update_role':
        roles[action['role_id']] = action['old_role']
    elif action['type'] == 'delete_role':
        roles[action['role_id']] = action['deleted_role']
    elif action['type'] == 'add_note':
        notes[action['note_id']] = action['old_note']
    elif action['type'] == 'delete_note':
        notes[action['note_id']] = action['deleted_note']
    elif action['type'] == 'delete_shift_note':
        shift_notes[action['note_id']] = action['deleted_note']
    elif action['type'] == 'update_shift_note':
        shift_notes[action['note_id']] = action['old_note']
    print("Откат выполнен.")
