from rich.columns import Columns
from rich.panel import Panel

from panels.abstract_panel import AbstractPanel
from config import WS_BORDER


class Workspace(AbstractPanel):
    def __init__(self, height, title="Workspace"):
        super().__init__(title)
        self.height = height

    def render(self):
        list_panels = [ls.render() for ls in self.children]
        lists = Columns(list_panels, expand=True)
        return Panel(lists, title=self.title, title_align="left",
                     expand=True, height=self.height, box=WS_BORDER)

    def save(self, out_file_dir='.'):
        filename = self.title.lower().replace(' ', '-')
        with open(f'{out_file_dir}/{filename}.md', 'w') as out:
            out.write(f'# {self.title}\n')

            for ls in self.children:
                ls.save(out)

    def get_selected_list(self):
        for ls in self.children:
            if ls.is_selected == True:
                return ls

    def get_selected_task(self):
        selected_list = self.get_selected_list()
        return selected_list.get_selected_task()
