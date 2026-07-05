# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: ShiftBoard
def multi_field_search(data, query):
    if not query:
        return data
    q = query.lower().strip()
    results = []
    for item in data:
        text_parts = [str(item.get(k, '')) for k in ('name', 'role', 'notes')]
        combined_text = ' '.join(text_parts)
        if q in combined_text or any(q == part.lower() for part in text_parts):
            results.append(item)
    return results
