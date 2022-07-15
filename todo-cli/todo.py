#! /home/zyrrus/.virtualenvs/todo-cli/bin/python

import sys

from runtime.display_manager import DisplayManager
import config


def main():
    config.read_config()
    dm = DisplayManager()

    if len(sys.argv) > 1:
        dm.run_tui(sys.argv[1])
    else:
        dm.run_cli()


if __name__ == '__main__':
    main()
