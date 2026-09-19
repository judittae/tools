# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: ShiftBoard
def self_check():
    """Финальная самопроверка ShiftBoard: тесты всех сущностей и вывод отчёта о готовности."""
    print("=" * 60)
    print("  ShiftBoard — самопроверка приложения")
    print("=" * 60)
    errors = []
    try:
        from shiftboard import (
            Role, Employee, Shift, Note, Replacement, BoardState,
            shift_valid, role_valid, employee_valid, note_valid,
            replacement_valid, board_valid, print_report
        )
        assert Role("manager") is not None
        assert Employee("Alice", "manager") is not None
        assert Shift("morning", 0, 8, "Alice") is not None
        assert Note("Привет", 10, "Alice") is not None
        assert Replacement("Bob", "morning", 1, "Alice") is not None
        assert shift_valid(Shift("morning", 0, 8, "Alice")) is True
        assert role_valid(Role("manager")) is True
        assert employee_valid(Employee("Alice", "manager")) is True
        assert note_valid(Note("Привет", 10, "Alice")) is True
        assert replacement_valid(Replacement("Bob", "morning", 1, "Alice")) is True
        assert board_valid(BoardState()) is True
        print_report(errors)
        print("\n✅ Все проверки пройдены. Приложение готово к использованию!\n")
    except Exception as e:
        print(f"\n❌ Ошибка самопроверки: {e}\n")
        raise
