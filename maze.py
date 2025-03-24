from gui import Line, Point
import time

class Cell():
    def __init__(self, x1, y1, x2, y2, window, top=True, left=True, bottom=True, right=True):
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.has_left_wall = left
        self.has_right_wall = right
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
    
    def draw(self, fill):
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill)
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill)
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill)
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill)

    def draw_move(self, to_cell, undo=False):
        self_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        self._win.draw_line(Line(self_center, to_center), "red" if undo else "grey")


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                c = Cell(self._x1 + self._cell_size_x * i,
                         self._y1 + self._cell_size_y * j,
                         self._x1 + self._cell_size_x * (i + 1),
                         self._y1 + self._cell_size_y * (j + 1),
                         self._win)
                col.append(c)
                c.draw("black")
                self._animate()
            self._cells.append(col)
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
