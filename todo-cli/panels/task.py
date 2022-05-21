from rich.panel import Panel
from rich.text import Text

from panels.abstract_panel import AbstractPanel
from config import TASK_ICON, TS_BORDER, TS_HIGHLIGHT, COMPACT_TASKS


class Task(AbstractPanel):
    def __init__(self, title="Task"):
        super().__init__(title)

    def render(self):
        if COMPACT_TASKS:
            return Text(f'{TASK_ICON} {self.title}', style=TS_HIGHLIGHT if self.is_selected else "none", no_wrap=False)
        return Panel(f'{TASK_ICON} {self.title}', style=TS_HIGHLIGHT if self.is_selected else "none", box=TS_BORDER)

    def save(self, out):
        out.write(f'- {self.title}\n')
