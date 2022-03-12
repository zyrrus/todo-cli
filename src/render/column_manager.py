import os

from constants import Keys
from render.column import Column
from utils.print_utils import StyledText
from utils.input_utils import cycle_in_range


class ColumnManager:
    def __init__(self):
        self.col_count = 0
        self.focused = 0
        self.selected = 1
        self.is_holding = False
        self.columns = []
        self.title = ''

        self.os_size = os.get_terminal_size()
        self.term_height = self.os_size.lines - 3

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
        if Keys.is_equal(user_input, Keys.leave):
            return
        elif Keys.is_equal(user_input, Keys.select):
            held = self.columns[self.focused]
            self.is_holding = not self.is_holding
            held.set_hold(self.is_holding)
        elif Keys.is_equal(user_input, Keys.up):
            self.selected = cycle_in_range(
                self.selected - 1, 0, self.term_height - 2)
        elif Keys.is_equal(user_input, Keys.down):
            self.selected = cycle_in_range(
                self.selected + 1, 0, self.term_height - 2)
        elif Keys.is_equal(user_input, Keys.left):
            self.focused = cycle_in_range(
                self.focused - 1, 0, self.col_count - 1)
        elif Keys.is_equal(user_input, Keys.right):
            self.focused = cycle_in_range(
                self.focused + 1, 0, self.col_count - 1)

        for col in self.columns:
            col.set_focus(False)

        highlight = self.columns[self.focused]
        highlight.set_focus(True)
        highlight.set_selected(self.selected)

    def log(self):
        for i, col in enumerate(self.columns):
            with open(f'log-{i}.txt', 'a') as logger:
                logger.write(col.log())
