import os

import click
import termcolor

from rendering.column_manager import ColumnManager
from utilities.storage import Storage


def main():
    path = './src/data/workspaces.json'

    storage = Storage(path)

    cm = ColumnManager()
    cm.render()

    # Temporary: prevents termination (clear output on close)
    input()


if __name__ == '__main__':
    main()
