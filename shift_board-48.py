# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: ShiftBoard
def _parse_shift_entry(raw: str):
    """Parse 'employee:role:hours:from:to' into a dict or raise ValueError."""
    parts = raw.split(':')
    if len(parts) != 5:
        raise ValueError(f"Invalid shift format, expected 5 fields")
    return {
        'employee': parts[0].strip(),
        'role': parts[1].strip(),
        'hours': int(parts[2].strip()),
        'from': parts[3].strip(),
        'to': parts[4].strip(),
    }

def _format_shift_entry(shift: dict) -> str:
    """Format a shift dict back to 'employee:role:hours:from:to'."""
    return f"{shift['employee']}:{shift['role']}:{shift['hours']}:{shift['from']}:{shift['to']}"

def _shift_conflicts(shifts: list) -> list:
    """Return list of (i, j) pairs where two shifts overlap in time and share an employee."""
    conflicts = []
    for i in range(len(shifts)):
        for j in range(i + 1, len(shifts)):
            s1, s2 = shifts[i], shifts[j]
            if s1['employee'] != s2['employee']:
                continue
            if s1['from'] < s2['to'] and s2['from'] < s1['to']:
                conflicts.append((i, j))
    return conflicts

def _deduplicate_notes(notes: list) -> list:
    """Return unique notes, preserving first-seen order."""
    seen = set()
    result = []
    for note in notes:
        if note not in seen:
            seen.add(note)
            result.append(note)
    return result
