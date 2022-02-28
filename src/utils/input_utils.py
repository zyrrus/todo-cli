from pynput.keyboard import KeyCode


def key(char):
    return KeyCode.from_char(char)


def cycle_in_range(i, start, stop):
    if start <= i <= stop:
        return i
    elif start > i:
        return stop
    return start
