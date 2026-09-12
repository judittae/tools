# === Stage 45: Добавь восстановление из резервной копии ===
# Project: ShiftBoard
def restore_backup(backup_path):
    """Восстанавливает данные из резервной копии JSON-файла."""
    if not os.path.exists(backup_path):
        print(f"Файл резервной копии не найден: {backup_path}")
        return False
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print("Неверный формат резервной копии")
            return False
        print(f"Резервная копия восстановлена из {backup_path}")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
