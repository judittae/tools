# === Stage 43: Добавь пагинацию длинных списков ===
# Project: ShiftBoard
def paginate(items, page_size=10):
    """Compact paginator that yields (index, item) pairs for a page."""
    total_pages = (len(items) + page_size - 1) // page_size
    for i in range(total_pages):
        start = i * page_size
        end = start + page_size
        yield (i, items[start:end])
