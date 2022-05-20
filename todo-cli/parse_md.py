from config import SELECTED_ICON
from panels.workspace import Workspace
from panels.list import List
from panels.task import Task


def get_ws_from_md(md_filepath, ws_height):
    ls_height = ws_height - 2
    ws = Workspace(ws_height)

    with open('todo.md') as in_file:
        last_list = None

        for line in in_file:
            # Handle empty lines
            line = line.strip('\n')
            if len(line) == 0:
                continue

            # Parse List
            if line.startswith('##'):
                ls_name = line[2:].strip()
                last_list = List(ls_height, ls_name)
                ws.add_child(last_list)
            # Parse Workspace
            elif line.startswith('#'):
                ws_name = line[1:].strip()
                ws.rename(ws_name)
            # Parse Task
            elif line.startswith('-'):
                ts_name = line[1:].strip()
                # Mark selected task + list
                if ts_name.startswith(SELECTED_ICON):
                    task = Task(ts_name[1:].strip())
                    task.set_selected(True)
                    last_list.set_selected(True)
                else:
                    task = Task(ts_name)
                last_list.add_child(task)

    return ws
