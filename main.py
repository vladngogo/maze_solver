import logging
from maze import Maze
from graphics import Window

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    m1 = Maze(
        x1=margin,
        y1=margin,
        num_rows=num_rows,
        num_cols=num_cols,
        cell_size_x=cell_size_x,
        cell_size_y=cell_size_y,
        win=win,
    )

    m1.solve()

    win.wait_for_close()


if __name__ == "__main__":
    logger.info("app started")
    main()
