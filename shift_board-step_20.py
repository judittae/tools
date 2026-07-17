# === Stage 20: Добавь восстановление записей из архива ===
# Project: ShiftBoard
def restore_from_archive(archive_path, output_dir):
    """Восстанавливает записи из архива в директорию."""
    import shutil, os
    if not os.path.exists(archive_path) or not os.path.isdir(output_dir):
        return False
    for root, dirs, files in os.walk(archive_path):
        rel = os.path.relpath(root, archive_path)
        dest = os.path.join(output_dir, rel)
        if rel == '.':
            continue
        os.makedirs(dest, exist_ok=True)
        for f in files:
            shutil.copy2(os.path.join(root, f), os.path.join(dest, f))
    return True
