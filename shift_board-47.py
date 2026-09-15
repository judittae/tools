# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: ShiftBoard
def demo():
    """Показать основной пользовательский сценарий."""
    print("=== ShiftBoard Demo ===\n")

    # 1. Создаём сотрудников
    staff = [
        Employee("Алексей", "dev", 160, 100),
        Employee("Мария", "dev", 150, 100),
        Employee("Дмитрий", "dev", 140, 100),
        Employee("Елена", "hr", 120, 100),
    ]
    print(f"Сотрудники: {len(staff)}")
    for s in staff:
        print(f"  {s.name} — роль={s.role}, зарплата={s.salary}")

    # 2. Создаём роли
    roles = [
        Role("Разработчик", "dev", 1000, 200),
        Role("HR-менеджер", "hr", 800, 150),
    ]
    print(f"\nРоли: {len(roles)}")
    for r in roles:
        print(f"  {r.title} — зарплата={r.salary}, часовая ставка={r.hourly_rate}")

    # 3. Создаём часы
    hours = [
        Hour("09:00", "17:00", "ПН"),
        Hour("09:00", "17:00", "ВТ"),
        Hour("09:00", "17:00", "СР"),
        Hour("09:00", "17:00", "ЧТ"),
        Hour("09:00", "17:00", "ПТ"),
    ]
    print(f"\nЧасы: {len(hours)}")
    for h in hours:
        print(f"  {h.start}-{h.end} {h.day}")

    # 4. Создаём смену
    shift = Shift("Смена 1", "dev", "09:00", "17:00", "ПН", 8.0, "Алексей")
    print(f"\nСмена: {shift}")

    # 5. Создаём замену
    replacement = Replacement("Алексей", "Дмитрий", "ПН", "09:00", "17:00")
    print(f"Замена: {replacement}")

    # 6. Создаём заметку
    note = Note("Плановая уборка офиса", "Елена", "09:30", "10:00")
    print(f"Заметка: {note}")

    # 7. Показываем расчёт зарплаты
    salary = calculate_salary(shift)
    print(f"\nЗарплата за смену: {salary:.2f}")

    # 8. Показываем расчёт за замены
    replacement_cost = calculate_replacement_cost(replacement)
    print(f"Стоимость замены: {replacement_cost:.2f}")

    # 9. Показываем расчёт за заметку
    note_cost = calculate_note_cost(note)
    print(f"Стоимость заметки: {note_cost:.2f}")

    # 10. Показываем общий отчёт
    print("\n=== Общий отчёт ===")
    print(f"Всего сотрудников: {len(staff)}")
    print(f"Всего ролей: {len(roles)}")
    print(f"Всего часов: {len(hours)}")
    print(f"Всего смен: {len(shifts)}")
    print(f"Всего замен: {len(replacements)}")
    print(f"Всего заметок: {len(notes)}")
    print("\nDemo завершён успешно!")
