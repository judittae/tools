# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: ShiftBoard
def switch_profile(new_name):
    """Переключить активный профиль пользователя."""
    if not new_name:
        print("Имя профиля не может быть пустым.")
        return False
    
    profiles = get_profiles()
    for prof in profiles:
        if prof['name'].lower() == new_name.lower():
            set_active_profile(prof['id'])
            print(f"Профиль '{new_name}' активирован.")
            return True
    
    print(f"Профиль '{new_name}' не найден.")
    return False
