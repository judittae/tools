# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: ShiftBoard
def get_next_action(state: dict) -> str:
    """Recommend the next step based on the current state of ShiftBoard."""
    if not state:
        return "Start by creating the first employee."
    if "employees" not in state or not state["employees"]:
        return "Add employees to the system."
    if "roles" not in state or not state["roles"]:
        return "Define job roles for the employees."
    if "shifts" not in state or not state["shifts"]:
        return "Create a shift schedule."
    if "replacements" not in state or not state["replacements"]:
        return "Allow employees to swap shifts."
    if "notes" not in state or not state["notes"]:
        return "Add notes or comments to the schedule."
    return "All core features are implemented. Consider adding a web interface or persistence layer."
