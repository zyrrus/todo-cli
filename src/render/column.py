from utils.print_utils import StyledText


class Column:
    def __init__(self, title, data):
        self.width = 0
        self.title = StyledText(title)
        self.contents = [StyledText(line) for line in data]

    def set_width(self, width):
        self.width = width

    def render(self, line_number):
        if line_number == 0:
            return self.title.full_pad(self.width).style(attrs=['bold'], color='blue')
        if line_number >= len(self.contents):
            return ''
        return self.contents[line_number].full_pad(self.width)
