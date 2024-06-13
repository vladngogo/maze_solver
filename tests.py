import unittest
from maze import Maze

num_rows = 12
num_cols = 10


class Tests(unittest.TestCase):
    def test_maze_create_cell(self):
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_break_entrance_and_exit(self):
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall, False)

    def test_reset_visited(self):
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertFalse(m1._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()
