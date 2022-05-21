from rich.console import Console
from rich.live import Live

from input_handler import InputHandler
from parse_md import get_ws_from_md


def main():
    console = Console()

    ws_height = console.height - 1
    ws = get_ws_from_md('todo.md', ws_height)

    ih = InputHandler(ws)
    ih.ia.correct_selection()

    is_looping = True
    while is_looping:
        console.clear()
        console.print(ws.render())

        is_looping = ih.handle_inputs()

    console.clear()


if __name__ == '__main__':
    main()
