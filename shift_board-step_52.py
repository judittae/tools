# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: ShiftBoard
import json
from datetime import datetime

def export_shift_report(shifts, employees):
    """Экспорт отчёта по сменам в текстовом формате."""
    lines = ["=== Сводка по сменам ===", f"Дата отчёта: {datetime.now().strftime('%Y-%m-%d')}", ""]
    for shift in shifts:
        emp = next((e for e in employees if e["id"] == shift["employee_id"]), None)
        role = next((r for r in shift["roles"] if r["id"] == shift["role_id"]), None)
        line = f"[{shift['id']}] Смена: {shift['start'].strftime('%Y-%m-%d %H:%M')} - {shift['end'].strftime('%Y-%m-%d %H:%M')}"
        if emp:
            line += f" | Сотрудник: {emp['name']}"
        if role:
            line += f" | Роль: {role['title']}"
        if shift.get("duration"):
            line += f" | Длительность: {shift['duration']}"
        lines.append(line)
    lines.append("")
    return "\n".join(lines)
