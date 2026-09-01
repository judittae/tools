# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: ShiftBoard
import unittest


class TestShiftBoard(unittest.TestCase):
    def test_shift_creation(self):
        from shiftboard import ShiftBoard
        board = ShiftBoard()
        shift = board.create_shift("morning", "2024-01-15", 8)
        self.assertEqual(shift.role, "morning")
        self.assertEqual(shift.date, "2024-01-15")
        self.assertEqual(shift.hours, 8)

    def test_employee_assignment(self):
        from shiftboard import ShiftBoard
        board = ShiftBoard()
        shift = board.create_shift("morning", "2024-01-15", 8)
        board.assign_employee(shift, "Anna")
        self.assertEqual(shift.assigned_to, "Anna")

    def test_role_validation(self):
        from shiftboard import ShiftBoard
        board = ShiftBoard()
        with self.assertRaises(ValueError):
            board.create_shift("invalid_role", "2024-01-15", 8)

    def test_date_validation(self):
        from shiftboard import ShiftBoard
        board = ShiftBoard()
        with self.assertRaises(ValueError):
            board.create_shift("morning", "not-a-date", 8)

    def test_duplicate_shift_date(self):
        from shiftboard import ShiftBoard
        board = ShiftBoard()
        s1 = board.create_shift("morning", "2024-01-15", 8)
        s2 = board.create_shift("morning", "2024-01-15", 8)
        self.assertEqual(s1.id, s2.id)

    def test_note_addition(self):
        from shiftboard import ShiftBoard
        board = ShiftBoard()
        shift = board.create_shift("morning", "2024-01-15", 8)
        board.add_note(shift, "Start early", "Anna")
        notes = shift.notes
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].text, "Start early")
        self.assertEqual(notes[0].author, "Anna")


if __name__ == '__main__':
    unittest.main()
