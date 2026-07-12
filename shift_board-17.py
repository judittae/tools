# === Stage 17: Добавь группировку записей по категориям ===
# Project: ShiftBoard
def group_entries_by_category(entries):
    """Сгруппировать записи по категориям (shift, note, swap)."""
    categories = {"shift": [], "note": [], "swap": []}
    for entry in entries:
        cat = entry.get("category", "unknown")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(entry)
    return dict(sorted(categories.items()))


def render_grouped_table(grouped):
    """Отобразить сгруппированные записи в виде таблицы."""
    lines = ["Категория | Запись"]
    for cat, records in grouped.items():
        summary = f"{cat}: {len(records)}"
        if not records:
            continue
        sample = records[0]
        key_val = next(iter(sample))
        val_str = str(sample[key_val])[:30]
        lines.append(f"{cat} | {summary} (пример: {val_str})")
    return "\n".join(lines)


# Пример использования
sample_entries = [
    {"id": 1, "title": "Смена А", "category": "shift"},
    {"id": 2, "title": "Примечание", "category": "note"},
    {"id": 3, "title": "Замена Б", "category": "swap"},
]

grouped = group_entries_by_category(sample_entries)
print(render_grouped_table(grouped))
