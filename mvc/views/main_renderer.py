from rich.console import Console

from models.panels import Workspace
from controllers.cursor import Cursor


class MainRenderer:
    def __init__(self, workspace=None):
        self.console = Console()
        self.workspace = workspace if workspace is not None else Workspace()
        self.cursor = Cursor()
