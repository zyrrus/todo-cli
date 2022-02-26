import os

from rendering.column import Column


class ColumnManager:
    def __init__(self, num_columns=5):
        os_size = os.get_terminal_size()
        self.term_width = os_size.columns - (os_size.columns % num_columns)
        self.term_height = os_size.lines - 1

        self.col_count = num_columns
        self.col_width = self.term_width // num_columns
        self.columns = [Column(self.col_width)] * num_columns

    def add_column(self, position=-1):
        pass

    def remove_column(self, position=-1):
        pass

    def render(self):
        for line_number in range(self.term_height):
            print('\r', end='')
            for col in self.columns:
                print(f'{col.render(line_number)}', end='')
            print()
