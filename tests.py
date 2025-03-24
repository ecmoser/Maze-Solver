import unittest, time
from maze import Maze
from window import Window

test_win = Window(1000, 1000)
test_maze = Maze(10, 10, 10, 10, 50, 50, test_win)

class Tests(unittest.TestCase):
    def test_maze_dimensions(self):
        self.assertEqual(len(test_maze._cells), 10)
        self.assertEqual(len(test_maze._cells[0]), 10)

    def test_maze_cell_dimensions(self):
        c = test_maze._cells[0][0]
        self.assertEqual(c._x2 - c._x1, 50)
        self.assertEqual(c._y2 - c._y1, 50)

    def test_maze_entrance_exit(self):
        test_maze._break_entrance_and_exit()
        entrance_c = test_maze._cells[0][0]
        exit_c = test_maze._cells[-1][-1]
        self.assertEqual(entrance_c.has_left_wall, False)
        self.assertEqual(exit_c.has_right_wall, False)

if __name__ == "__main__":
    unittest.main()

