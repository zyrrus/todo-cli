from rich import box
from rich.table import Table
from rich.text import Text


class WorkspaceRenderer:
    def __init__(self, workspace):
        self.ws_json = workspace

    def render(self, console):
        title = self.ws_json['name']
        columns = self.ws_json['columns']
        unsorted_column_data = []
        max_column_len = 0

        table = Table(title=title, expand=True, box=box.SIMPLE)

        for column in columns:
            table.add_column(column["title"])

            data = column["data"]
            unsorted_column_data.append(data)
            if len(data) > max_column_len:
                max_column_len = len(data)

        # Pad shorter columns with empty strings
        # (so zip() doesn't break)
        for column in unsorted_column_data:
            if len(column) < max_column_len:
                diff = max_column_len - len(column)
                for _ in range(diff):
                    column.append("")

        sorted_column_data = zip(*unsorted_column_data)

        for line in sorted_column_data:
            line = [Text(text, style='bold magenta blink') for text in line]
            table.add_row(*line)

        console.print(table)
