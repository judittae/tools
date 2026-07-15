# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: ShiftBoard
def archive_records(records, cutoff_date=None):
    """Archive records older than the given date into a single string."""
    if not records:
        return "[]\n"
    if cutoff_date is None:
        cutoff_date = datetime.now().date()
    archived = [r for r in records if r.get("date") and r["date"] < cutoff_date]
    active = [r for r in records if r.get("date") or not r.get("date")]
    if not archived:
        return "[]\n"
    lines = ["# Archived Records\n"]
    for i, rec in enumerate(archived, 1):
        key = ", ".join(f"{k}={v}" for k, v in rec.items())
        lines.append(f"Record_{i}={{ {key} }}")
    return "\n".join(lines) + "\n"
