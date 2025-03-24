from gui import Line, Point

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