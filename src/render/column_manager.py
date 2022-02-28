import os

from pynput.keyboard import Key

from render.column import Column
from utils.print_utils import StyledText
from utils.input_utils import cycle_in_range, key


HEADER_SIZE = 1


class ColumnManager:
    def __init__(self):
        self.col_count = 0
        self.focused = 0
        self.selected = 1
        self.columns = []
        self.title = ''

        self.os_size = os.get_terminal_size()
        self.term_height = self.os_size.lines - 2 - HEADER_SIZE

    def calc_dimensions(self):
        self.term_width = self.os_size.columns - \
            (self.os_size.columns % self.col_count)

        self.col_width = self.term_width // self.col_count

        for col in self.columns:
            col.set_width(self.col_width)

    def init_data(self, workspace):
        self.title = StyledText(workspace['name'])
        self.focused = 0
        for col in workspace['columns']:
            self.add_column(col)
        self.columns[self.focused].set_focus(True)

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

    def update(self, user_input):
        if user_input == key('q'):
            return
        elif user_input == Key.up:
            self.selected = cycle_in_range(
                self.selected - 1, 0, self.term_height)
        elif user_input == Key.down:
            self.selected = cycle_in_range(
                self.selected + 1, 0, self.term_height)
        elif user_input == Key.left:
            pass
        elif user_input == Key.right:
            pass

        highlight = self.columns[self.focused]
        highlight.set_focus(True)
        highlight.set_selected(self.selected)

    def log(self):
        for i, col in enumerate(self.columns):
            with open(f'log-{i}.txt', 'a') as logger:
                logger.write(col.log())
