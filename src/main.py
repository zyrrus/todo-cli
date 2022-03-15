import os

import termcolor

from constants import STORAGE_PATH
from render.column_manager import ColumnManager
from utils.storage import Storage
from utils.print_utils import clear
from event_loop import EventLoop


def main():
    el = EventLoop(STORAGE_PATH)
    el.loop()


if __name__ == '__main__':
    main()
