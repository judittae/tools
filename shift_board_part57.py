# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: ShiftBoard
def mass_delete(items, ids):
    """Массовое удаление с подтверждением через параметр.

    items - коллекция объектов со списком атрибутов для подтверждения.
    ids - список идентификаторов для удаления.
    Возвращает список удалённых элементов.
    """
    if not ids:
        return []
    to_delete = [i for i in items if i.id in ids]
    if len(to_delete) != len(ids):
        confirm = input("Удалить {} из {} выбранных? (y/N): ".format(len(to_delete), len(ids)))
    else:
        confirm = input("Удалить {} выбранных? (y/N): ".format(len(to_delete)))
    if confirm.strip().lower() not in ('y', 'yes'):
        return []
    for item in to_delete:
        print("[удалено] {}".format(item))
    return to_delete
