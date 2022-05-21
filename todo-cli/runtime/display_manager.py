from rich.console import Console
from rich.live import Live

from config import DEFAULT_PATH
from parse_md import get_ws_from_md
from runtime.input_handler import InputHandler


class DisplayManager:
    def __init__(self):
        self.console = Console()
        self.workspace_height = self.console.height - 1
        self.save_location = DEFAULT_PATH

    def run_cli(self, prev_ws=None):
        commands = {
            'help': '',
            'open': '',
            'make': ''
        }

    def run_tui(self, filename):
        ws = get_ws_from_md(filename, self.workspace_height)

        ih = InputHandler(ws)
        ih.ia.correct_selection()

        is_looping = True
        while is_looping:
            self.console.clear()
            self.console.print(ws.render())

            is_looping = ih.handle_inputs()

        self.console.clear()

        should_save = self.console.input("Would you like to save? [Y/n] ")
        if not should_save.lower().startswith('n'):
            self.console.print(f"Saved to {ws.save(self.save_location)}")


'''
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
    '''
