from rich.columns import Columns
from rich.panel import Panel

from panels.abstract_panel import AbstractPanel
from config import WS_BORDER


class Workspace(AbstractPanel):
    def __init__(self, height, title="Workspace"):
        super().__init__(title)
        self.height = height
        self.subtitle = ''

    def render(self):
        list_panels = [ls.render() for ls in self.children]
        lists = Columns(list_panels, expand=True)
        return Panel(lists, title=self.title, title_align="left", subtitle=self.subtitle,
                     height=self.height, box=WS_BORDER)

    def save(self, out_file_dir='.'):
        filename = self.title.lower().replace(' ', '-')
        full_path = f'{out_file_dir}/{filename}.md'
        with open(full_path, 'w') as out:
            out.write(f'# {self.title}\n')

            for ls in self.children:
                ls.save(out)

        return full_path

    def get_selected_list(self):
        for i, ls in enumerate(self.children):
            if ls.is_selected == True:
                return ls, i
        return None, -1

    def get_selected_task(self):
        selected_list, ls_i = self.get_selected_list()
        if selected_list is not None:
            selected_task, ts_i = selected_list.get_selected_task()
            return selected_task, ls_i, ts_i
        return None, -1, -1

    def set_subtitle(self, subtitle):
        self.subtitle = subtitle