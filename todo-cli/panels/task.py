from rich.panel import Panel
from rich.text import Text

import config
from panels.abstract_panel import AbstractPanel


class Task(AbstractPanel):
    def __init__(self, title="Task"):
        super().__init__(title)

    def render(self):
        if config.get('COMPACT_TASKS'):
            return Text(f'{config.get("TASK_ICON")} {self.title}', style=config.get('TS_HIGHLIGHT') if self.is_selected else "none", no_wrap=False)
        return Panel(f'{config.get("TASK_ICON")} {self.title}', style=config.get('TS_HIGHLIGHT') if self.is_selected else "none", box=config.get("TS_BORDER"))

    def save(self, out):
        out.write(f'- {self.title}\n')
