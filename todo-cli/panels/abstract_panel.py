from abc import ABC, abstractmethod


class AbstractPanel(ABC):
    def __init__(self, title):
        self.title = title
        self.children = []
        self.is_selected = False

    def rename(self, new_name):
        self.title = new_name

    def add_child(self, panel, index=None):
        if index is None:
            self.children.append(panel)
        else:
            self.children.insert(index + 1, panel)

    def remove_child(self, index=-1):
        self.children.pop(index)

    def set_selected(self, is_selected):
        self.is_selected = is_selected

    @abstractmethod
    def render(self):
        raise NotImplementedError("Panel needs a render method")

    @abstractmethod
    def save(self, out_file):
        raise NotImplementedError("Panel needs a save method")
