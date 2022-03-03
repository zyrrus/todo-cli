from enum import Enum

from pynput.keyboard import Key, KeyCode


STORAGE_PATH = './src/data/workspaces.json'


def key(char):
    return KeyCode.from_char(char)


class Keys(Enum):
    leave = [Key.esc, key('q')]
    select = [Key.enter]
    up = [Key.up, key('w')]
    left = [Key.left, key('a')]
    down = [Key.down, key('s')]
    right = [Key.right, key('d')]

    @staticmethod
    def is_equal(received, desired):
        return received in desired.value

    @staticmethod
    def is_valid(other):
        for item in Keys:
            if other in item.value:
                return True
        return False
