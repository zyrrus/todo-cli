from utils.print_utils import StyledText
from utils.input_utils import cycle_in_range


class Column:
    def __init__(self, title, data):
        self.line_number = 0

        self.selected = 0
        self.is_focused = False
        self.is_held = False

        self.width = 0
        self.title = StyledText(title)
        self.contents = [StyledText(line) for line in data]

    def set_width(self, width):
        self.width = width

    def set_selected(self, i):
        self.selected = i

    def set_focus(self, focus):
        self.is_focused = focus

    def set_hold(self, should_hold):
        self.is_held = should_hold

    def set_text(self, text):
        self.contents[self.selected] = StyledText(text)

    def render(self, line_number):
        line_number -= 1

        # Title
        if line_number == -1:
            return self.title.full_pad(self.width).style(attrs=['bold'], color='blue')

        # Render body
        text = StyledText('').full_pad(self.width) if line_number >= len(
            self.contents) else self.contents[line_number].padded().full_pad(self.width)

        if line_number == self.selected:
            # Render held
            if self.is_held:
                return text.style(attrs=['bold', 'blink'], on_color='on_yellow')
            # Render selected
            elif self.is_focused:
                return text.style(attrs=['bold'], on_color='on_red')

        return text

    def log(self):
        return f"Focus: {self.is_focused}; Selected: {self.selected}; Contents: {(self.contents)}\n"
