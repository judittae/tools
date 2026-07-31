# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: ShiftBoard
def get_app_config():
    config = {
        "max_shifts_per_day": 3,
        "min_rest_between_shifts_hours": 8,
        "default_shift_length_minutes": 480,
        "timezone": "UTC",
        "language": "ru",
        "role_hierarchy": {"manager": ["supervisor", "employee"]},
    }
    return config
