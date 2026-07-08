# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: ShiftBoard
def weekly_stats(employees, hours):
    """Считает недельную статистику по дате для каждого сотрудника."""
    stats = {}
    for emp in employees:
        start_date = emp.get("start_date")
        if not start_date:
            continue
        current_week = datetime.strptime(start_date, "%Y-%m-%d").isocalendar()[:2]
        if current_week not in stats:
            stats[current_week] = {}
        for h in hours:
            emp_name = h.get("employee")
            if emp_name and emp_name == emp["name"] and h["date"].startswith(start_date.split("-")[0]):
                year, week = datetime.strptime(h["date"], "%Y-%m-%d").isocalendar()[:2]
                if (year, week) not in stats:
                    stats[(year, week)] = {}
                if emp_name not in stats[(year, week)]:
                    stats[(year, week)][emp_name] = 0
                stats[(year, week)][emp_name] += h.get("hours", 0)
    return stats
