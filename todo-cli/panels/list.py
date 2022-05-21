from rich.console import Group
from rich.panel import Panel

from panels.abstract_panel import AbstractPanel
from config import LS_BORDER, LS_HIGHLIGHT


class List(AbstractPanel):
    def __init__(self, height, title="List"):
        super().__init__(title)
        self.height = height

    def render(self):
        selected = LS_HIGHLIGHT if self.is_selected else "none"
        task_panels = [ts.render() for ts in self.children]
        tasks = Group(*task_panels)
        return Panel(tasks, title=self.title, title_align="left", height=self.height, box=LS_BORDER, style=selected)

    def save(self, out):
        out.write(f'\n## {self.title}\n\n')

        for ls in self.children:
            ls.save(out)

    def get_selected_task(self):
        for i, task in enumerate(self.children):
            if task.is_selected == True:
                return task, i
        return None, -1

    def set_selected(self, is_selected):
        super().set_selected(is_selected)
        if is_selected:
            # If selected, select a child too
            if len(self.children) > 0:
                self.children[0].set_selected(True)
        else:
            selected_task, _ = self.get_selected_task()
            if selected_task is not None:
                selected_task.set_selected(False)
