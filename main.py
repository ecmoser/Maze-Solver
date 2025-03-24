from window import Window
from gui import Point, Line

test_points = (Point(50, 50), Point(50, 100), Point(100, 100), Point(100, 50))

def main():
    win = Window(800, 600)
    for i in range(len(test_points)):
        a = i
        b = (i + 1) % len(test_points)
        win.draw_line(Line(test_points[a], test_points[b]), "black")
    win.wait_for_close()

main()