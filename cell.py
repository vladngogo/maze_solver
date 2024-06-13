import logging
from graphics import Point, Line

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Cell:
    def __init__(self, win, _x1=None, _y1=None, _x2=None, _y2=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = _x1
        self._y1 = _y1
        self._x2 = _x2
        self._y2 = _y2
        self._win = win
        self.visited = False

    def draw(self):
        if self.has_left_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(line, fill_color=fill_color)

        if self.has_right_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(line, fill_color=fill_color)

        if self.has_top_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(line, fill_color=fill_color)

        if self.has_bottom_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(line, fill_color=fill_color)

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        from_x = (self._x1 + self._x2) / 2
        from_y = (self._y1 + self._y2) / 2

        to_x = (to_cell._x1 + to_cell._x2) / 2
        to_y = (to_cell._y1 + to_cell._y2) / 2

        logger.info(f"moving from [{from_x},{from_y}] to [{to_x},{to_y}]")
        move_line = Line(Point(from_x, from_y), Point(to_x, to_y))
        self._win.draw_line(move_line, fill_color)
