from rich import box

# Path where .md files are located and saved
DEFAULT_PATH = '.'

# Border styles
# box.{ASCII, DOUBLE, HEAVY, ROUNDED, SQUARE}
WS_BORDER = box.ROUNDED
LS_BORDER = box.ROUNDED
TS_BORDER = box.ROUNDED

# Character that shows up next to each task in the TUI
__icons = '›»⦁♥♡'
TASK_ICON = __icons[1]

# Color when item is highlighted
TS_HIGHLIGHT = 'red'
LS_HIGHLIGHT = 'blue'

# Display tasks with a border or as a single line
COMPACT_TASKS = True

# Prompt when renaming each item
WORKSPACE_PROMPT = 'Rename workspace> '
LIST_PROMPT = 'Rename list> '
TASK_PROMPT = 'Rename task> '

# Placeholder name when creating new item
NEW_LIST_NAME = '...'
NEW_TASK_NAME = '...'
