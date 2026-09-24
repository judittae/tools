# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: ShiftBoard
import json

def load_text_records(filepath):
    records = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
    current = {}
    for line in lines:
        line = line.strip()
        if not line:
            if current:
                records.append(current)
                current = {}
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            current[key.strip()] = val.strip()
    if current:
        records.append(current)
    return records

def save_text_records(records, filepath):
    with open(filepath, 'w') as f:
        for r in records:
            for k, v in r.items():
                f.write(f"{k}: {v}\n")
            f.write("\n")
