# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: ShiftBoard
def delete_record(table_name, record_id):
    if not table_name or not record_id:
        raise ValueError("Таблица и ID записи обязательны")
    
    try:
        with open('shiftboard.db', 'r') as f:
            lines = f.readlines()
        
        new_lines = []
        deleted_count = 0
        
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) < 2:
                continue
            
            record_id_str = parts[1]
            
            try:
                current_id = int(record_id_str)
                
                # Если ID совпадает, пропускаем строку (удаляем запись)
                if current_id == int(record_id):
                    deleted_count += 1
                    continue
                
                new_lines.append(line)
            except ValueError:
                # Пропускаем строки, где ID не является числом
                pass
        
        with open('shiftboard.db', 'w') as f:
            f.writelines(new_lines)
        
        return deleted_count > 0
    
    except FileNotFoundError:
        print(f"Файл базы данных '{table_name}.db' не найден.")
        return False
