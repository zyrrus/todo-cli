import curses
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

from config import SELECTED_ICON
from panels import Workspace, List, Task
from parse_md import get_ws_from_md


def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getkey()
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)


def main(stdsrc):
    console = Console()
    console.clear()

    ws_height = console.height - 1 - 3
    ws = get_ws_from_md('todo.md', ws_height)

    console.print(ws.render())
    ws.save('./todo-cli')


if __name__ == '__main__':
    curses.wrapper(main)
