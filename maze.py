from gui import Line, Point
import time

class Cell():
    def __init__(self, x1, y1, x2, y2, window, top=True, left=True, bottom=True, right=True):
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.has_left_wall = left
        self.has_right_wall = right
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = window
    
    def draw(self, fill):
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), fill)
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), fill)
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), fill)
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), fill)

    def draw_move(self, to_cell, undo=False):
        self_center = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        to_center = Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)
        self.__win.draw_line(Line(self_center, to_center), "red" if undo else "grey")


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__create_cells()

    def __create_cells(self):
        self.__cells = []
        for i in range(self.__num_cols):
            col = []
            for j in range(self.__num_rows):
                c = Cell(self.__x1 + self.__cell_size_x * i,
                         self.__y1 + self.__cell_size_y * j,
                         self.__x1 + self.__cell_size_x * (i + 1),
                         self.__y1 + self.__cell_size_y * (j + 1),
                         self.__win)
                col.append(c)
                c.draw("black")
                self.__animate()
            self.__cells.append(col)
    
    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
