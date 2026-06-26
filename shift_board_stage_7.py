# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: ShiftBoard
def sort_shifts(shifts, key_type='date'):
    if not shifts: return []
    reverse = True
    def get_sort_key(s):
        val = s.get(key_type)
        if isinstance(val, str): return (0, val.lower())
        if isinstance(val, int): return (1, -val)
        return (2, '')
    sorted_shifts = sorted(shifts, key=get_sort_key, reverse=reverse)
    return sorted_shifts
