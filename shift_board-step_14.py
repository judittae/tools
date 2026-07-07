# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: ShiftBoard
def generate_shiftboard_summary():
    """Генерирует краткую текстовую сводку по текущим данным."""
    lines = []
    
    # Сводка сотрудников
    active_count = sum(1 for s in employees if s.status == "active")
    inactive_count = len(employees) - active_count
    lines.append(f"Всего сотрудников: {len(employees)} (активных: {active_count}, неактивных: {inactive_count})")
    
    # Сводка ролей
    role_stats = {}
    for r in roles:
        role_stats[r.name] = {"count": 0, "hours_total": 0}
    for e in employees:
        if e.role and e.role.name in role_stats:
            role_stats[e.role.name]["count"] += 1
    
    lines.append(f"Роли с сотрудниками:")
    for name, stats in sorted(role_stats.items()):
        lines.append(f"  - {name}: {stats['count']} сотрудников")
    
    # Сводка смен за неделю
    week_hours = {}
    for shift in shifts:
        date_key = shift.start.date().isoformat()
        if date_key not in week_hours:
            week_hours[date_key] = 0
        week_hours[date_key] += shift.hours
    
    lines.append(f"Смены за неделю ({len(week_hours)} дней):")
    for date, hours in sorted(week_hours.items()):
        lines.append(f"  - {date}: {hours}ч")
    
    # Сводка замен
    if replacements:
        total_replacements = sum(len(r) for r in replacements.values())
        lines.append(f"Замены: {total_replacements}")
    else:
        lines.append("Замены: нет")
    
    # Сводка заметок
    notes_by_date = {}
    for note in shift_notes:
        date_key = note.date.isoformat() if hasattr(note, 'date') else "unknown"
        if date_key not in notes_by_date:
            notes_by_date[date_key] = []
        notes_by_date[date_key].append(note.text[:50])
    
    lines.append(f"Заметки ({len(notes)}):")
    for date, texts in sorted(notes_by_date.items()):
        lines.append(f"  - {date}: " + "; ".join(texts))
    
    return "\n".join(lines)
