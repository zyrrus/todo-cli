from rich.console import Group
from rich.panel import Panel

from panels.abstract_panel import AbstractPanel
from config import LS_BORDER


class List(AbstractPanel):
    def __init__(self, height, title="List"):
        super().__init__(title)
        self.height = height

    def render(self):
        task_panels = [ts.render() for ts in self.children]
        tasks = Group(*task_panels)
        return Panel(tasks, title=self.title, title_align="left", height=self.height, box=LS_BORDER)

    def save(self, out):
        out.write(f'\n## {self.title}\n\n')

        for ls in self.children:
            ls.save(out)
