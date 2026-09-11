# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: ShiftBoard
def backup_file(filepath, backup_dir="backups"):
    """Создать резервную копию файла данных в директории backups."""
    import os, shutil, datetime
    if not os.path.exists(filepath):
        return False
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(filepath)}.bak_{timestamp}")
    try:
        shutil.copy2(filepath, backup_path)
        return True
    except Exception:
        return False
