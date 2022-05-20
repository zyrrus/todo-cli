from rich import box

# Border styles
# box.{ASCII, DOUBLE, HEAVY, ROUNDED, SQUARE}
WS_BORDER = box.ROUNDED
LS_BORDER = box.ROUNDED
TS_BORDER = box.ROUNDED

# Character that shows up next to each task in the TUI
__icons = '›»⦁♥♡'
TASK_ICON = __icons[1]

# Character that indicates which task was last selected
# Shouldn't be any characters that interfere with Markdown
SELECTED_ICON = '!'

# Color when task is highlighted
TS_HIGHLIGHT = 'red'
LS_HIGHLIGHT = 'blue'
