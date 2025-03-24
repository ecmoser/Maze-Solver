import unittest
from maze import Maze
from window import Window

test_win = Window(1000, 1000)

class Tests(unittest.TestCase):
    def test_maze_dimensions(self):
        m = Maze(10, 10, 10, 10, 50, 50, test_win)
        self.assertEqual(len(m._cells), 10)
        self.assertEqual(len(m._cells[0]), 10)

    def test_maze_cell_dimensions(self):
        m = Maze(10, 10, 10, 10, 50, 50, test_win)
        c = m._cells[0][0]
        self.assertEqual(c._x2 - c._x1, 50)
        self.assertEqual(c._y2 - c._y1, 50)

if __name__ == "__main__":
    unittest.main()

