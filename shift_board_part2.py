# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: ShiftBoard
class ShiftBoardData:
    def __init__(self):
        self.employees = {}
        self.roles = {}
        self.shifts = []
        self.notes = {}
    
    def validate_employee_name(self, name):
        if not isinstance(name, str) or len(name.strip()) < 2:
            raise ValueError("Имя сотрудника должно быть строкой длиной не менее 2 символов.")
        return True
    
    def validate_role_name(self, role_name):
        if not isinstance(role_name, str) or len(role_name.strip()) < 3:
            raise ValueError("Название роли должно быть строкой длиной не менее 3 символов.")
        return True
    
    def validate_shift_duration(self, hours):
        if not isinstance(hours, (int, float)) or hours <= 0 or hours > 24:
            raise ValueError("Длительность смены должна быть числом от 1 до 24 часов.")
        return True
    
    def validate_date_format(self, date_str):
        import datetime
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD.")

def register_employee(data, name, role_name=None):
    data.validate_employee_name(name)
    if not data.employees.get(name):
        data.employees[name] = {"role": None}
    if role_name and data.roles.get(role_name):
        data.employees[name]["role"] = role_name

def register_role(data, name, hours_per_shift=8):
    data.validate_role_name(name)
    data.validate_shift_duration(hours_per_shift)
    data.roles[name] = {"hours": hours_per_shift}

def create_shift(data, employee_name, role_name=None, start_date="2023-10-01", duration=8):
    if not data.employees.get(employee_name):
        raise ValueError(f"Сотрудник {employee_name} не найден.")
    if role_name and not data.roles.get(role_name):
        raise ValueError(f"Роль {role_name} не найдена.")
    
    shift_id = len(data.shifts) + 1
    new_shift = {
        "id": shift_id,
        "employee": employee_name,
        "role": role_name or data.employees[employee_name].get("role"),
        "start_date": start_date,
        "duration": duration,
        "notes": ""
    }
    data.shifts.append(new_shift)

def add_note(data, shift_id, note_text):
    if not isinstance(note_text, str) or len(note_text.strip()) > 500:
        raise ValueError("Заметка должна быть строкой длиной не более 500 символов.")
    
    for shift in data.shifts:
        if shift["id"] == shift_id:
            existing_notes = shift.get("notes", "")
            if existing_notes and note_text.strip() not in existing_notes:
                shift["notes"] = f"{existing_notes}\n{note_text}"
            else:
                shift["notes"] = note_text
            return True
    raise ValueError
