from abc import ABC, abstractclassmethod


class Panel(ABC):
    def __init__(self, title=""):
        self.title = title

    def rename(self, new_title):
        self.title = new_title


class ParentPanel(Panel):
    def __init__(self, title=""):
        super().__init__(title)

    @abstractclassmethod
    def add_child(self, child):
        raise NotImplementedError()
