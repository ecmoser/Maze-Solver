from gui import Line, Point
import time, random

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
        self.visited = False
    
    def draw(self, fill):
        empty_fill = "white"
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), empty_fill)
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), empty_fill)
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill)
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), empty_fill)
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill)
        else:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), empty_fill)

    def draw_move(self, to_cell, undo=False):
        self_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        self._win.draw_line(Line(self_center, to_center), "red" if undo else "grey")


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if not seed is None:
            random.seed(seed)

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
                self._animate()
            self._cells.append(col)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(-1, -1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            directions = []
            if j - 1 >= 0 and self._cells[i][j-1].visited == False:
                directions.append("up")
            if j+1 < len(self._cells[i]) and self._cells[i][j+1].visited == False:
                directions.append("down")
            if i-1 >= 0 and self._cells[i-1][j].visited == False:
                directions.append("left")
            if i+1 < len(self._cells) and self._cells[i+1][j].visited == False:
                directions.append("right")
            if len(directions) == 0:
                self._draw_cell(i, j)
                return
            choice = random.choice(directions)
            match choice:
                case "up":
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
                    self._break_walls_r(i, j-1)
                case "down":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
                    self._break_walls_r(i, j+1)
                case "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                    self._break_walls_r(i-1, j)
                case "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                    self._break_walls_r(i+1, j)


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _draw_cell(self, i, j):
        self._cells[i][j].draw("black")
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def solve(self):
        return self.solve_r(0, 0)
    
    def solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        if j-1 >= 0 and self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self.solve_r(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        if j+1 < len(self._cells[i]) and self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self.solve_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        if i-1 >= 0 and self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self.solve_r(i-1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        if i+1 >= 0 and self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self.solve_r(i+1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        return False