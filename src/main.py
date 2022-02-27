import os

import click
import termcolor

from render.column_manager import ColumnManager
from utils.storage import Storage
from utils.print_utils import clear


def main():
    path = './src/data/workspaces.json'

    storage = Storage(path)

    cm = ColumnManager()
    cm.render()

    # Temporary: prevents termination (clear output on close)
    input()
    clear()


if __name__ == '__main__':
    main()
