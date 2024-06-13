import logging
import random
import time
from cell import Cell

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        logger.info(
            f"initializing maze with {self._num_rows} rows and {self._num_cols} columns"
        )
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        logger.info(
            f"maze created with {len(self._cells)} rows and {len(self._cells[0])} columns"
        )
        self._reset_cells_visited()
        logger.info(f"resetting visited cells")

    def _create_cells(self):
        for i in range(self._num_rows):
            row_cells = []
            for j in range(self._num_cols):
                x1 = self._x1 + j * self._cell_size_x
                y1 = self._y1 + i * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                row_cells.append(
                    Cell(
                        _x1=x1,
                        _y1=y1,
                        _x2=x2,
                        _y2=y2,
                        win=self._win,
                    )
                )
            self._cells.append(row_cells)

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # check up
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # check down
            if i + 1 < self._num_rows and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # check right
            if j + 1 < self._num_cols and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            # check left
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            next = random.choice(to_visit)

            # up
            if next[0] < i:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            # down
            if next[0] > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            # right
            if next[1] > j:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
            # left
            if next[1] < j:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False

            self._draw_cell(i, j)
            self._draw_cell(next[0], next[1])

            self._break_walls_r(next[0], next[1])

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        # check up
        if (
            i - 1 >= 0
            and not self._cells[i - 1][j].visited
            and self._cells[i][j].has_top_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cells[i - 1][j].draw_move(self._cells[i][j], undo=True)
        # check down
        if (
            i + 1 < self._num_rows
            and not self._cells[i + 1][j].visited
            and self._cells[i][j].has_bottom_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cells[i + 1][j].draw_move(self._cells[i][j], undo=True)
        # check right
        if (
            j + 1 < self._num_cols
            and not self._cells[i][j + 1].visited
            and self._cells[i][j].has_right_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cells[i][j + 1].draw_move(self._cells[i][j], undo=True)
        # check left
        if (
            j - 1 >= 0
            and not self._cells[i][j - 1].visited
            and self._cells[i][j].has_left_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cells[i][j - 1].draw_move(self._cells[i][j - 1], undo=True)

        return False

    def solve(self):
        self._solve_r(0, 0)
