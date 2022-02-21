import os

from column import Column


class ColumnManager:
    def __init__(self, num_columns=5):
        self.term_width = os.get_terminal_size().columns - \
            (os.get_terminal_size().columns % num_columns)
        self.term_height = os.get_terminal_size().lines - 1

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
