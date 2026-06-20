# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: ShiftBoard
class ShiftBoard:
    def __init__(self):
        self._data = {'employees': [], 'roles': [], 'shifts': []}
    
    def add_employee(self, name: str, role: str) -> None:
        if not any(e['name'] == name for e in self._data['employees']):
            self._data['employees'].append({'id': len(self._data['employees']) + 1, 'name': name, 'role': role})
    
    def add_role(self, title: str) -> None:
        if not any(r['title'] == title for r in self._data['roles']):
            self._data['roles'].append({'id': len(self._data['roles']) + 1, 'title': title})
    
    def add_shift(self, employee_id: int, role_id: int, start_time: str, end_time: str) -> None:
        if not any(e['id'] == employee_id for e in self._data['employees']):
            raise ValueError(f"Employee {employee_id} not found")
        if not any(r['id'] == role_id for r in self._data['roles']):
            raise ValueError(f"Role {role_id} not found")
        existing = next((s for s in self._data['shifts'] 
                         if s['employee_id'] == employee_id and s['start_time'] == start_time), None)
        if existing:
            return
        new_shift = {'id': len(self._data['shifts']) + 1, 'employee_id': employee_id, 'role_id': role_id, 
                     'start_time': start_time, 'end_time': end_time}
        self._data['shifts'].append(new_shift)
