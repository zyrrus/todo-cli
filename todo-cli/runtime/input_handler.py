from getkey import getkey, keys

from config import TASK_PROMPT, LIST_PROMPT, WORKSPACE_PROMPT, NEW_LIST_NAME, NEW_TASK_NAME
from panels.list import List
from panels.task import Task


class InputHandler:
    def __init__(self, workspace=None):
        self.ia = InputActions(workspace)
        self.task_move_mode = False
        self.list_move_mode = False
        

        persistent_keys = {
            'q': self.ia.quit,
            keys.CTRL_S: self.ia.save_workspace,
            keys.ENTER: self.toggle_task_move_mode,
            keys.SINGLE_QUOTE: self.toggle_list_move_mode,
        }
        self.key_map = {
            **persistent_keys,
    
            'L': self.ia.add_list,
            'T': self.ia.add_task,
            keys.CTRL_L: self.ia.remove_list,
            keys.CTRL_T: self.ia.remove_task,

            'w': self.ia.rename_workspace,
            'l': self.ia.rename_list,
            't': self.ia.rename_task,

            keys.UP: self.ia.prev_task,
            keys.DOWN: self.ia.next_task,
            keys.LEFT: self.ia.prev_list,
            keys.RIGHT: self.ia.next_list,

            'task_move_mode': {
                **persistent_keys,

                keys.UP: self.ia.shift_task_up,
                keys.DOWN: self.ia.shift_task_down,
                keys.LEFT: self.ia.shift_task_left,
                keys.RIGHT: self.ia.shift_task_right,
            },

            'list_move_mode': {
                **persistent_keys,

                keys.LEFT: self.ia.shift_list_left,
                keys.RIGHT: self.ia.shift_list_right,
            }
        }

    def handle_inputs(self):
        self.ia.correct_selection()

        key = getkey()
        should_quit = False

        action_map = self.key_map
        if self.task_move_mode:
            action_map = self.key_map['task_move_mode']
        elif self.list_move_mode:
            action_map = self.key_map['list_move_mode']

        if key in action_map:
            should_quit = action_map[key]() or False

        return not should_quit

    def toggle_task_move_mode(self):
        self.task_move_mode = not self.task_move_mode

        # Disable the other mode if it was active when
        # activating the current mode
        if self.list_move_mode and self.task_move_mode:
            self.list_move_mode = False

        self.ia.ws.set_subtitle('task move mode active' if self.task_move_mode else '')

    def toggle_list_move_mode(self):
        self.list_move_mode = not self.list_move_mode

        # Disable the other mode if it was active when
        # activating the current mode
        if self.task_move_mode and self.list_move_mode:
            self.task_move_mode = False

        self.ia.ws.set_subtitle('list move mode active' if self.list_move_mode else '')


class InputActions:
    def __init__(self, workspace):
        self.ws = workspace

    # File I/O

    def quit(self):
        return True

    def save_workspace(self):
        self.ws.save()

    # Rename

    def rename_workspace(self):
        new_ws_name = input(WORKSPACE_PROMPT)
        if new_ws_name.strip() != '':
            self.ws.rename(new_ws_name.strip())

    def rename_list(self):
        ls, _ = self.ws.get_selected_list()
        if ls is not None:
            new_ls_name = input(LIST_PROMPT)
            if new_ls_name.strip() != '':
                ls.rename(new_ls_name.strip())

    def rename_task(self):
        ts, _, _ = self.ws.get_selected_task()
        if ts is not None:
            new_ts_name = input(TASK_PROMPT)
            if new_ts_name.strip() != '':
                ts.rename(new_ts_name.strip())

    # Creation/Deletion

    def add_list(self):
        new_list = List(self.ws.height - 2, NEW_LIST_NAME)

        ls, ls_i = self.ws.get_selected_list()
        index = ls_i if ls is not None else None

        self.ws.add_child(new_list, index)
        
        self.next_list()
        self.rename_list()

    def add_task(self, rename=True):
        new_task = Task(NEW_TASK_NAME)

        ts, ls_i, ts_i = self.ws.get_selected_task()
        if ls_i >= 0:
            index = ts_i if ts is not None else None
            self.ws.children[ls_i].add_child(new_task, index)

            self.next_task()
            if rename:
                self.rename_task()

    def remove_list(self):
        ls, ls_i = self.ws.get_selected_list()
        self.next_list()
        if ls is not None:
            self.ws.remove_child(ls_i)

    def remove_task(self):
        task, ls_i, ts_i = self.ws.get_selected_task()
        self.next_task()
        if task is not None:
            self.ws.children[ls_i].remove_child(ts_i)

    # Change selection

    def next_list(self):
        self._change_list_selection(1)

    def prev_list(self):
        self._change_list_selection(-1)

    def next_task(self):
        self._change_task_selection(1)

    def prev_task(self):
        self._change_task_selection(-1)

    # Swap items

    def shift_task_up(self): 
        self._vertical_task_shift(-1)

    def shift_task_down(self): 
        self._vertical_task_shift(1)

    def shift_task_left(self): 
        self._horizontal_task_shift(-1)

    def shift_task_right(self): 
        self._horizontal_task_shift(1)

    def shift_list_left(self): 
        self._list_shift(-1)

    def shift_list_right(self): 
        self._list_shift(1)

    # Utilities

    def _vertical_task_shift(self, delta):
        task, ls_i, ts_i = self.ws.get_selected_task()
        if task is not None:
            ls = self.ws.children[ls_i]
            if len(ls.children) > 1: 
                next_ts_i = cycle(ts_i + delta, len(ls.children))
                ls.children[ts_i], ls.children[next_ts_i] = ls.children[next_ts_i], ls.children[ts_i]

    def _horizontal_task_shift(self, delta): 
        old_task, _, _ = self.ws.get_selected_task()
        if old_task is not None:
            self.remove_task()
            if delta < 0:
                self.prev_list()
            else:
                self.next_list()

            self.add_task()
            new_task, _, _ = self.ws.get_selected_task()
            new_task.rename(old_task.title)

    def _list_shift(self, delta): 
        ls, ls_i = self.ws.get_selected_list()
        if len(self.ws.children) > 1:
            next_ls_i = cycle(ls_i + delta, len(self.ws.children))
            self.ws.children[ls_i], self.ws.children[next_ls_i] = self.ws.children[next_ls_i], self.ws.children[ls_i]

    def _change_list_selection(self, delta):
        old, ls_i = self.ws.get_selected_list()
        if old is not None:
            old.set_selected(False)
            new_ls_i = cycle(ls_i + delta, len(self.ws.children))
            self.ws.children[new_ls_i].set_selected(True)

    def _change_task_selection(self, delta):
        old, ls_i, ts_i = self.ws.get_selected_task()
        if old is not None:
            old.set_selected(False)
            ls = self.ws.children[ls_i]
            new_ts_i = cycle(ts_i + delta, len(ls.children))
            ls.children[new_ts_i].set_selected(True)

    def correct_selection(self):
        task, ls_i, ts_i = self.ws.get_selected_task()

        if ls_i < 0 and len(self.ws.children) > 0:
            ls = self.ws.children[0]
            ls.set_selected(True)

            if ts_i < 0 and len(ls.children) > 0:
                ts = ls.children[0]
                ts.set_selected(True)


def cycle(value, list_len):
    # Keep indices in range of a list while only incr/decr value
    # for list_len = 3 -> 1, 2, 0, 1, 2, 0, ...
    if 0 <= value < list_len:
        return value
    return value + (list_len if value < 0 else -list_len)
