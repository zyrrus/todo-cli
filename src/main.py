import os

from pynput.keyboard import Key
from rich.console import Console

from render.workspace_renderer import WorkspaceRenderer
from utils.storage import Storage
from utils.input_manager import InputManager


class Cursor:
    def __init__(self):
        self.state = 'none'

    def on_up(self):
        self.state = 'up'
        self.say()

    def on_down(self):
        self.state = 'down'
        self.say()

    def on_left(self):
        self.state = 'left'
        self.say()

    def on_right(self):
        self.state = 'right'
        self.say()

    def say(self):
        print(self.state)


def main():
    s = Storage('./src/data/workspaces.json')
    wr = WorkspaceRenderer(s.data["workspaces"][0])

    console = Console()

    console.clear()
    wr.render(console)
    # input()
    # console.clear()


def main1():
    cursor = Cursor()
    hotkeys = {
        frozenset([Key.up]): cursor.on_up,
        frozenset([Key.down]): cursor.on_down,
        frozenset([Key.left]): cursor.on_left,
        frozenset([Key.right]): cursor.on_right,
    }
    im = InputManager(hotkeys)
    im.start()


if __name__ == '__main__':
    main1()
