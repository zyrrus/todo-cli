from rich.console import Console
from rich.live import Live

from input_handler import InputHandler
from parse_md import get_ws_from_md


def main():
    console = Console()
    ws_height = console.height - 1

    ws = get_ws_from_md('todo.md', ws_height)
    ih = InputHandler(ws)

    with Live(ws.render(), auto_refresh=False, transient=True) as live:
        is_looping = True
        ih.ia.correct_selection()
        while is_looping:
            console.clear()
            console.print(ws.render())

            is_looping = ih.handle_inputs()

            live.refresh()


if __name__ == '__main__':
    main()
