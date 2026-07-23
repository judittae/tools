# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: ShiftBoard
def print_shift_record(record):
    if not record:
        return
    r = record[0]
    name, role, start, end, notes = r['name'], r.get('role', '—'), r.get('start', '—'), r.get('end', '—'), r.get('notes', '')
    hours = (r.get('end_time') - r.get('start_time')) / 3600 if all(k in r for k in ('start_time','end_time')) else '—'
    swap_type = r.get('swap_type', '') or ''
    swap_note = f" — {r['swap_reason']}" if r.get('swap_type') and r.get('swap_reason') else ''
    print(f"[{name}] [{role}] {start} → {end} ({hours:.1f}ч){' | ' + swap_type + swap_note}{': ' + notes}  ")

for rec in records:
    print_shift_record(rec)
