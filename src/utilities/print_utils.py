from termcolor import colored
from os import get_terminal_size, name, system


def clear():
    system('clear' if name == 'nt' else 'cls')


class StyledText:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.__str__()

    def padded(self, padding=1, left=True, right=False):
        if left:
            self.text = self.text.rjust(padding)
        if right:
            self.text = self.text.ljust(padding)
        return self

    def full_pad(self, width, justification='left'):
        if justification == 'left':
            self.text = self.text.ljust(width)
        elif justification == 'right':
            self.text = self.text.rjust(width)
        else:
            self.text = self.text.center(width)
        return self

    def style(self, **kwargs):
        # Arguments:
        # attrs=[bold, dark, underline, blink, reverse, concealed]
        # color=grey, red, green, yellow, blue, magenta, cyan, white
        # on_color=on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white

        self.text = colored(self.text, **kwargs)
        return self


def main():
    text = StyledText('hi there, this is a test.')
    print(
        text.full_pad(get_terminal_size().columns, justification='center')
            .style(attrs=['dark'], color=None, on_color='on_red')
    )


if __name__ == '__main__':
    main()
