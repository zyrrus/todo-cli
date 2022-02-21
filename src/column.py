class Column:
    def __init__(self, width):
        self.width = width
        self.contents = 'abcdefghijklmnopqrstuvwxyz'

    def render(self, line_number):
        if line_number >= len(self.contents):
            return ''
        return self.contents[line_number].ljust(self.width)
