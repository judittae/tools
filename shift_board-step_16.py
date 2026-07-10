# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: ShiftBoard
def monthly_stats():
    stats = {}
    for day in range(31):
        date = datetime(2025, 1, day)
        shifts = get_shifts(date)
        notes = get_notes(date)
        stats[date] = {
            'shifts': len(shifts),
            'notes': len(notes),
            'total_hours': sum(s.hours for s in shifts if hasattr(s, 'hours'))
        }
    return stats
