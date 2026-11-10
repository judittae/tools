# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: ShiftBoard
def bulk_update_selected(ops):
    """Применяет массовое обновление к выбранным записям.

    ops - список кортежей (id, ...) в порядке, соответствующем
    количеству полей в записи. Если передан список списков, применяется
    как массив: все записи с тем же индексом получают одинаковые значения.
    """
    if not ops:
        return
    ids = [r[0] for r in ops]
    if len(set(ids)) != len(ids):
        raise ValueError("У записей не могут быть одинаковые id")
    for rec in data:
        if rec["id"] in ids:
            idx = ids.index(rec["id"])
            if isinstance(ops, list) and isinstance(ops[0], (list, tuple)) and len(ops) == len(ids):
                values = ops[idx]
            else:
                values = ops[idx]
            for k, v in values.items():
                rec[k] = v
            rec["updated_at"] = now()
