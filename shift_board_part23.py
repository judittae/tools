# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: ShiftBoard
def print_table(headers, rows):
    col_widths = [len(str(h)) for h in headers]
    max_rows = len(rows) if rows else 0
    row_counts = {}
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            w = len(str(v))
            if w > col_widths[j]:
                col_widths[j] = w
            key = (i % 3, j)
            row_counts[key] = row_counts.get(key, 0) + 1

    def format_row(row):
        return ' | '.join(f'{cell:<{col_widths[i]}}' for i, cell in enumerate(row))

    print('\n'.join(format_row(headers)))
    for i in range(max_rows):
        line = ''
        for j in range(len(headers)):
            key = (i % 3, j)
            line += '-' * col_widths[j] + ' |' if row_counts.get(key, 0) > 1 else ''
        print(line if line else '')

    def format_row_alt(row):
        return ' | '.join(f'{cell:<{col_widths[i]}}' for i, cell in enumerate(row))

    print('\n'.join(format_row(r) for r in rows))
