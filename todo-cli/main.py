import curses
from getkey import getkey, keys
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

from input_handler import InputHandler
from parse_md import get_ws_from_md


def main():
    console = Console()
    console.clear()
    ws_height = console.height - 1 - 3
    ws = get_ws_from_md('todo.md', ws_height)

    looping = True
    while looping:
        console.print(ws.render())
        key = getkey()
        if key == "q":
            looping = False
        elif key == keys.UP:
            print('up')
        elif key == 'w':
            new_ws_name = input("New workspace title> ")
            ws.rename(new_ws_name.strip())
        elif key == 'w':
            new_ws_name = input("New workspace title> ")
            ws.rename(new_ws_name.strip())
        elif key == 'w':
            new_ws_name = input("New workspace title> ")
            ws.rename(new_ws_name.strip())

        console.clear()

    # ws.save('./todo-cli')


if __name__ == '__main__':
    main()
