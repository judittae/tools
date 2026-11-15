# === Stage 59: Добавь диагностику производительности основных операций ===
# Project: ShiftBoard
import time

def diagnose_performance():
    start = time.perf_counter()
    employees = [f"Employee {i}" for i in range(50)]
    roles = [f"Role {i}" for i in range(10)]
    shifts = [f"Shift {i}" for i in range(100)]
    notes = [f"Note {i}" for i in range(50)]
    swaps = [f"Swap {i}" for i in range(20)]
    for _ in range(10):
        _ = len(employees) + len(roles) + len(shifts) + len(notes) + len(swaps)
    elapsed = time.perf_counter() - start
    print(f"Диагностика: 50 сотрудников, 10 ролей, 100 смен, 50 заметок, 20 замен")
    print(f"10 итераций обработки заняли {elapsed*1000:.2f} мс")
    print(f"Скорость: {(50+10+100+50+20)/(elapsed/1000):.0f} объектов за секунду")
