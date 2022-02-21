import os

import click
import termcolor

from column_manager import ColumnManager


def main():
    cm = ColumnManager()
    cm.render()

    # Temporary: prevents termination (clear output on close)
    input()


if __name__ == '__main__':
    main()
