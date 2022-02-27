def get_cur_workspace(data):
    cur_selected = data['selected']
    workspace = data['workspaces'][cur_selected]
    return workspace


def get_columns(workspace):
    return len(workspace['columns'])
