# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: ShiftBoard
def dry_run(operation, entity, old_state, new_state):
    """Log a dry-run operation without applying it.
    
    Args:
        operation: Type of operation ('add', 'update', 'delete')
        entity: The entity being operated on
        old_state: Current state before operation
        new_state: Proposed state after operation
    """
    if not dry_run_mode:
        return
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'operation': operation,
        'entity': str(entity),
        'old_state': old_state,
        'new_state': new_state,
        'status': 'dry-run'
    }
    dry_run_log.append(log_entry)
