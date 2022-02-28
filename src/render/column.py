from utils.print_utils import StyledText
from utils.input_utils import cycle_in_range


class Column:
    def __init__(self, title, data):
        self.line_number = 0

        self.selected = 0
        self.is_focused = False
        self.width = 0
        self.title = StyledText(title)
        self.contents = [StyledText(line) for line in data]

    def set_width(self, width):
        self.width = width

    def set_selected(self, i):
        self.selected = i

    def set_focus(self, focus):
        self.is_focused = focus

    def render(self, line_number):
        line_number -= 1
        if line_number == -1:
            return self.title.full_pad(self.width).style(attrs=['bold'], color='blue')

        text = StyledText('').full_pad(self.width) if line_number >= len(
            self.contents) else self.contents[line_number].padded().full_pad(self.width)

        if self.is_focused and line_number == self.selected:
            return text.style(attrs=['bold'], on_color='on_red')
        return text

    def log(self):
        return f"Focus: {self.is_focused}; Selected: {self.selected}; Contents: {(self.contents)}\n"
