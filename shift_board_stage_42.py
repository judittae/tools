# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: ShiftBoard
import sys

def color(text: str, fg: int = 0, bg: int = 0) -> str:
    """Apply ANSI color codes to *text* (default: no color)."""
    if fg is None and bg is None:
        return text
    if sys.stdout.isatty():
        return f"\033[{40 + bg}m\033[{30 + fg}m{text}\033[0m"
    return text

# ── ANSI palette ─────────────────────────────────────────────────────────────
# fg: 0=black 1=red 2=green 3=yellow 4=blue 5=magenta 6=cyan 7=white
# bg: 1=red 2=green 3=yellow 4=blue 5=magenta 6=cyan 7=white

def fg_red(s: str) -> str: return color(s, 1)
def fg_green(s: str) -> str: return color(s, 2)
def fg_yellow(s: str) -> str: return color(s, 3)
def fg_blue(s: str) -> str: return color(s, 4)
def fg_cyan(s: str) -> str: return color(s, 6)
def fg_white(s: str) -> str: return color(s, 7)
def bg_red(s: str) -> str: return color(s, 0, 1)
def bg_green(s: str) -> str: return color(s, 0, 2)
