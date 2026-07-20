# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: ShiftBoard
def check_overdue_reminders():
    now = datetime.datetime.now()
    overdue = []
    for shift in shifts:
        reminders = shift.get('reminders', [])
        for r in reminders:
            if r['time'] < now and r not in overdue:
                overdue.append(r)
    return overdue
