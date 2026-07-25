# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: ShiftBoard
def validate_date(date_str):
    """Парсит дату в формате YYYY-MM-DD, возвращает объект datetime.date или None."""
    import re
    pattern = r'^(\d{4})-(\d{2})-(\d{2})$'
    match = re.match(pattern, date_str)
    if not match:
        return None
    year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
    try:
        return datetime.date(year, month, day)
    except ValueError as e:
        print(f"Ошибка даты: {date_str}. Причина: {e}")
        return None

def format_date_error(date_obj):
    """Формирует понятное сообщение об ошибке для некорректной даты."""
    try:
        year, month, day = date_obj.year, date_obj.month, date_obj.day
        return f"Неверная дата {year}-{month}-{day}: такой день в этом месяце не существует."
    except Exception as e:
        return f"Ошибка формата даты: {date_str}. Проверьте формат YYYY-MM-DD."
