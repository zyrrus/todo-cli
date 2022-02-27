import os

from render.column import Column
from utils.print_utils import StyledText

HEADER_SIZE = 1


class ColumnManager:
    def __init__(self):
        self.col_count = 0
        self.columns = []
        self.title = ''

        self.os_size = os.get_terminal_size()
        self.term_height = self.os_size.lines - 1 - HEADER_SIZE

    def calc_dimensions(self):
        self.term_width = self.os_size.columns - \
            (self.os_size.columns % self.col_count)

        self.col_width = self.term_width // self.col_count

        for col in self.columns:
            col.set_width(self.col_width)

    def init_data(self, workspace):
        self.title = StyledText(workspace['name'])
        for col in workspace['columns']:
            self.add_column(col)

    def add_column(self, col_data):
        self.columns.append(Column(col_data['title'], col_data['data']))
        self.col_count += 1
        self.calc_dimensions()

    def remove_column(self):
        if len(self.columns) > 0:
            self.columns.pop()
            self.col_count -= 1
            self.calc_dimensions()

    def render(self):
        # Header
        styled_title = self.title.full_pad(self.term_width, justification='center').style(
            attrs=['bold', 'reverse'], color='cyan')
        print(f"\r{styled_title}")

        # Columns
        for line_number in range(self.term_height):
            print('\r', end='')
            for col in self.columns:
                print(f'{col.render(line_number)}', end='')
            print()
