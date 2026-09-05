# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: ShiftBoard
import argparse

def parse_cli():
    parser = argparse.ArgumentParser(description="ShiftBoard CLI")
    sub = parser.add_subparsers(dest="command")
    p_add = sub.add_parser("add", help="add a shift")
    p_add.add_argument("employee", help="employee name")
    p_add.add_argument("role", help="role")
    p_add.add_argument("start", help="start time (HH:MM)")
    p_add.add_argument("end", help="end time (HH:MM)")
    p_add.add_argument("--notes", default="", help="notes")
    p_del = sub.add_parser("del", help="delete a shift")
    p_del.add_argument("shift_id", help="shift ID")
    p_list = sub.add_parser("list", help="list all shifts")
    p_list.add_argument("--role", default=None, help="filter by role")
    p_list.add_argument("--employee", default=None, help="filter by employee")
    p_list.add_argument("--date", default=None, help="filter by date (YYYY-MM-DD)")
    return parser.parse_args()
