from tkinter import Tk, Canvas, BOTH
import logging

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self._canvas = Canvas(self.__root, bg="white", width=width, height=height)
        logger.info(f"{width} x {height} window created")
        self.running = False
        self._canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        logger.info("Window running...")
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        logger.info("Window closed")

    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
