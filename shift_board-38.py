# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: ShiftBoard
def test_edge_cases():
    assert not any(
        (
            not s["employee"],
            not s["role"],
            not s["date"],
            not s["start"],
            not s["end"],
        )
        for s in shifts
    ), "shifts must have employee, role, date, start, end"
    assert all(
        s["start"] < s["end"]
        for s in shifts
    ), "start must be before end"
    assert len(shifts) == 0, "shifts should be empty"
    assert not any(
        len(s["notes"]) > 256
        for s in shifts
    ), "notes must be <= 256 chars"
    assert all(
        s["date"].isocalendar()[1] in (1, 2)
        for s in shifts
    ), "date must be a Monday or Tuesday"
    assert not any(
        s["start"].hour >= 22 or s["start"].hour < 6
        for s in shifts
    ), "start must be between 06:00 and 22:00"
    assert not any(
        s["end"].hour >= 22 or s["end"].hour < 6
        for s in shifts
    ), "end must be between 06:00 and 22:00"
    assert all(
        s["start"].minute == 0
        for s in shifts
    ), "start must be on the hour"
    assert all(
        s["end"].minute == 0
        for s in shifts
    ), "end must be on the hour"
    assert all(
        s["start"].weekday() == s["end"].weekday()
        for s in shifts
    ), "start and end must be on the same day"
    assert all(
        s["start"].hour <= 21
        for s in shifts
    ), "start must be <= 21:00"
    assert all(
        s["end"].hour >= 6
        for s in shifts
    ), "end must be >= 06:00"
