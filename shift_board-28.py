# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: ShiftBoard
def print_shiftboard_metrics():
    shifts = Shift.get_all()
    employees = Employee.get_all()
    roles = Role.get_all()
    
    total_hours_worked = sum(s.hours for s in shifts)
    unique_employees_used = len(set(s.employee_id for s in shifts)) if shifts else 0
    coverage_score = (unique_employees_used / len(employees) * 100) if employees and unique_employees_used > 0 else 0
    
    cancelled_shifts = [s for s in shifts if s.status == 'cancelled']
    cancellation_rate = ((len(cancelled_shifts) / len(shifts)) * 100) if shifts else 0
    
    avg_shift_duration = (total_hours_worked / unique_employees_used) if unique_employees_used > 0 else 0
    
    print(f"Совокупные часы работы: {total_hours_worked}")
    print(f"Участников смен: {unique_employees_used} из {len(employees)} ({coverage_score:.1f}%)")
    print(f"Отмена смен: {len(cancelled_shifts)}/{len(shifts)} ({cancellation_rate:.1f}%)")
    print(f"Средняя длительность смены на сотрудника: {avg_shift_duration:.1f} ч")
