from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


def main():
    console = Console()
    console.clear()
    max_height = console.height - 1 - 3

    ls = Panel("- Task", title="List", title_align="left", height=max_height-2)
    lists = Columns([ls] * 4, expand=True)
    ws = Panel(lists, title="Workspace", title_align="left",
               expand=True, height=max_height)

    console.print(ws)


if __name__ == '__main__':
    main()
