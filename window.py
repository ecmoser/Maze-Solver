from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "maze"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(width=width, height=height, background="white")
        self.__canvas.pack()
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False