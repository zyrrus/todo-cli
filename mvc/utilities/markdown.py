from models.panels import Workspace, List, Task


def workspace_to_markdown(workspace, markdown_path):
    with open(markdown_path, 'w+') as file:
        file.write(str(workspace))


def markdown_to_workspace(markdown_path):
    def rm_empty(lines): return list(filter(None, lines))

    with open(markdown_path, 'r') as file:
        raw_lines = file.readlines()
        lines = rm_empty(map(lambda line: line.strip('\n').strip(), raw_lines))

        ws = Workspace()
        last_list = None

        for line in lines:
            if line.startswith('-'):
                ts_name = line[1:].strip()
                last_list.add_child(Task(ts_name))
            elif line.startswith('##'):
                if last_list is not None:
                    last_list.select(0)
                ls_name = line[2:].strip()
                last_list = List(ls_name)
                ws.add_child(last_list)
            elif line.startswith('#'):
                ws_name = line[1:].strip()
                ws.rename(ws_name)

        last_list.select(0)
        ws.select(0)

    return ws
