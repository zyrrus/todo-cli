from rich.panel import Panel

from panels.abstract_panel import AbstractPanel
from config import TASK_ICON, SELECTED_ICON, TS_BORDER


class Task(AbstractPanel):
    def __init__(self, title="Task"):
        super().__init__(title)

    def render(self):
        return Panel(f'{TASK_ICON} {self.title}', style="red" if self.is_selected else "none", box=TS_BORDER)

    def save(self, out):
        selected = SELECTED_ICON if self.is_selected else ''
        out.write(f'- {selected} {self.title}\n')
