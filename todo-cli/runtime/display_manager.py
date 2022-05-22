from rich.console import Console
from rich.live import Live
from rich.table import Table

from config import DEFAULT_PATH
from panels.workspace import Workspace
from panels.list import List
from panels.task import Task
from runtime.input_handler import InputHandler


class DisplayManager:
    def __init__(self):
        self.console = Console()
        self.workspace_height = self.console.height - 1
        self.save_location = DEFAULT_PATH
        self.help_text = self.generate_help_text()
        
        self.console.clear()

    def run_cli(self):
        aliases = {
            'help': ['help', 'h'],
            'open': ['open', 'o'],
            'make': ['make', 'm'],
            'quit': ['quit', 'q'],
        }

        while True:
            # Prompt user for command
            inp = self.console.input('todo-cli> ')
            inputs = inp.split()
            
            # Split command from any potential arguments
            inp = inputs[0].lower() if len(inputs) > 0 else inp
        
            # Run matching command
            if inp in aliases['help']: 
                self.console.print(self.help_text)
            elif inp in aliases['open']: 
                if len(inputs) == 2:
                    filename = inputs[1]
                    self.run_tui(filename)
                    break
                else:
                    self.console.print('Missing arguments for `open PATH_TO_MD` command', style='red')
            elif inp in aliases['make']: 
                if len(inputs) == 2:
                    self.save_location = inputs[1]
                self.run_tui()
                break 
            elif inp in aliases['quit']:
                break

    def run_tui(self, existing_file=None):
        # Load workspace
        if existing_file is not None:
            existing_file += '' if existing_file.endswith('.md') else '.md'
            ws = self.load_existing(existing_file)
        else:
            ws = self.create_new()

        # Initialize the keyboard input module
        ih = InputHandler(ws)
        ih.ia.correct_selection()

        # Begin event loop
        is_looping = True
        while is_looping:
            self.console.clear()
            self.console.print(ws.render())
            is_looping = ih.handle_inputs()
        self.console.clear()

        # Ask to save on quit
        should_save = self.console.input("Would you like to save? [Y/n] ")
        if not should_save.lower().startswith('n'):
            self.console.print(f"Saved to {ws.save(self.save_location)}")

    def generate_help_text(self):
        help_cmd = Table(title="Help - Available commands")
        help_cmd.add_column("cmd")
        help_cmd.add_column("args")
        help_cmd.add_column("description")
        help_cmd.add_row("help", "", 'Show available commands')
        help_cmd.add_row("open", "PATH_TO_MD", 'Open workspace using existing .md file')
        help_cmd.add_row("make", "[OUTPUT_DIR]", 'Create new workspace in default/defined directory')
        help_cmd.add_row("quit", "", 'Exit the program')
        return help_cmd

    def load_existing(self, md_filepath):
        ls_height = self.workspace_height - 2
        ws = Workspace(self.workspace_height)

        with open('todo.md') as in_file:
            last_list = None

            for line in in_file:
                # Handle empty lines
                line = line.strip('\n')
                if len(line) == 0:
                    continue
                # Parse List
                if line.startswith('##'):
                    ls_name = line[2:].strip()
                    last_list = List(ls_height, ls_name)
                    ws.add_child(last_list)
                # Parse Workspace
                elif line.startswith('#'):
                    ws_name = line[1:].strip()
                    ws.rename(ws_name)
                # Parse Task
                elif line.startswith('-'):
                    ts_name = line[1:].strip()
                    last_list.add_child(Task(ts_name))

        return ws

    def create_new(self):
        ws = Workspace(self.workspace_height)
        return ws