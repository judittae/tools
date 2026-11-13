# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: ShiftBoard
class View:
    """Простое пользовательское представление списка с базовыми операциями."""

    def __init__(self, name, columns=None):
        self.name = name
        self.columns = columns or []
        self.rows = []

    def add_row(self, data):
        self.rows.append(data)

    def remove_row(self, index):
        if 0 <= index < len(self.rows):
            del self.rows[index]

    def get_row(self, index):
        return self.rows[index] if 0 <= index < len(self.rows) else None

    def update_row(self, index, data):
        if 0 <= index < len(self.rows):
            self.rows[index] = data

    def sort(self, key):
        self.rows.sort(key=key)

    def filter(self, predicate):
        return [row for row in self.rows if predicate(row)]

    def count(self):
        return len(self.rows)

    def to_text(self):
        if not self.rows:
            return "Пусто"
        header = " | ".join(self.columns)
        lines = [header]
        for row in self.rows:
            lines.append(" | ".join(str(item) for item in row))
        return "\n".join(lines)


def register_view(view):
    global VIEWS
    VIEWS.append(view)


def get_view(name):
    for view in VIEWS:
        if view.name == name:
            return view
    return None


def list_views():
    return [v.name for v in VIEWS]
