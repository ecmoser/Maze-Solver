from window import Window
from gui import Point, Line
from maze import Cell, Maze

def draw_test_points(test_points, win):
    for i in range(len(test_points)):
        a = i
        b = (i + 1) % len(test_points)
        win.draw_line(Line(test_points[a], test_points[b]), "black")

def draw_test_cells(test_cells, win):
    for cell in test_cells:
        cell.draw("black")

def main():
    win = Window(800, 600)
    test_points = (Point(200, 200), Point(200, 250), Point(250, 250), Point(250, 200))
    test_cells = (Cell(50, 50, 100, 100, win),
                  Cell(110, 50, 160, 100, win, top=False, bottom=False),
                  Cell(50, 110, 100, 160, win, left=False, right=False),
                  Cell(110, 110, 160, 160, win, False, False, False, False))
    test_maze = Maze(10, 10, 10, 10, 50, 50, win)

    test_maze._break_entrance_and_exit()
    test_maze._break_walls_r(0,0)
    test_maze._reset_cells_visited()
    test_maze.solve()
    win.wait_for_close()

main()