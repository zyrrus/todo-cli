import os
import json

from rich import box

_config = {
    # Path where .md files are located and saved
    'DEFAULT_PATH': '/home/zyrrus/.todo',

    # TODO: These can't be configured properly
    # Border styles
    # box.{ASCII, DOUBLE, HEAVY, ROUNDED, SQUARE}
    'WS_BORDER': box.ROUNDED,
    'LS_BORDER': box.ROUNDED,
    'TS_BORDER': box.ROUNDED,

    # Character that shows up next to each task in the TUI
    # › » ⦁ ♥ ♡
    'TASK_ICON': '»',

    # Style when item is highlighted
    'TS_HIGHLIGHT': 'bold red',
    'LS_HIGHLIGHT': 'blue',

    # Style when item is in move mode
    'TS_MOVE': 'reverse',
    'LS_MOVE': 'reverse',

    # Display tasks with a border or as a single line
    'COMPACT_TASKS': True,

    # Prompt when renaming each item
    'CLI_PROMPT': 'todo-cli> ',
    'WORKSPACE_PROMPT': 'Rename workspace> ',
    'LIST_PROMPT': 'Rename list> ',
    'TASK_PROMPT': 'Rename task> ',
    'NEW_LIST_PROMPT': 'Name new list> ',
    'NEW_TASK_PROMPT': 'Name new task> ',

    # Placeholder name when creating new item
    'NEW_LIST_NAME': '...',
    'NEW_TASK_NAME': '...',
}


def read_config():
    config_file = os.path.join(os.getcwd(), 'config.json')

    with open(config_file, 'r') as conf:
        f = json.load(conf)
        _config.update(f)


def get(config_str):
    return _config[config_str]
