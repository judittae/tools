# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: ShiftBoard
def show_menu():
    print("\n=== ShiftBoard Menu ===")
    print("1. Add Employee | 2. Assign Role | 3. Create Shift | 4. Swap Shifts | 5. Add Note | 6. View Schedule | 7. Exit")
    try:
        choice = input("Select option (1-7): ").strip()
        return int(choice) if choice.isdigit() else None
    except ValueError:
        print("Invalid input.")
        return None
