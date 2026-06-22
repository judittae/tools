# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: ShiftBoard
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in record_fields and key in records[record_id]:
            records[record_id][key] = value
        else:
            print(f"Неверное поле для редактирования: {key}")
    
    print(f"Запись с ID {record_id} успешно обновлена.")
    return True
