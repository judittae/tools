# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: ShiftBoard
def format_shift_entry(shift, employee, role):
    """Формирует читаемый текстовый блок для одной смены."""
    date = shift.get("date", "Без даты")
    start = shift.get("start", "")
    end = shift.get("end", "")
    duration = shift.get("duration", "")
    if start and end:
        duration = f"{start} → {end}"
    location = shift.get("location", "")
    notes = shift.get("notes", "")
    if notes:
        location = f"{location} [{notes}]" if location else notes
    return (
        f"📅 {date}\n"
        f"👤 {employee}\n"
        f"🎭 {role}\n"
        f"⏰ {duration}"
    )


def format_day_summary(day_data):
    """Собирает сводку по дню: занятость, замены, свободные слоты."""
    date = day_data.get("date", "Без даты")
    shifts = day_data.get("shifts", [])
    replacements = day_data.get("replacements", [])
    free_slots = day_data.get("free_slots", [])
    total = len(shifts) + len(replacements)
    free_text = f"\n🟢 Свободно: {free_slots}" if free_slots else ""
    return (
        f"📆 {date}\n"
        f"📊 В сумме: {total} записей\n"
        f"📋 {len(shifts)} смен"
        f"{free_text}"
    )


def format_full_report(all_days):
    """Формирует итоговый отчёт по всем дням планировки."""
    parts = []
    for day in all_days:
        parts.append(format_day_summary(day))
    return "\n\n".join(parts)


def print_board_report(all_shifts, all_employees, all_roles, all_days):
    """Выводит отформатированный отчёт на экран."""
    print("=" * 50)
    print("📊 Отчёт по рабочим сменам")
    print("=" * 50)
    print("\n👥 Сотрудники:")
    for emp in all_employees:
        print(f"  • {emp}")
    print("\n🎭 Роли:")
    for role in all_roles:
        print(f"  • {role}")
    print("\n📆 Дни планировки:")
    print(format_full_report(all_days))
    print("=" * 50)
