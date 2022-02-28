from time import sleep

from pynput.keyboard import Key, Events

from utils.input_utils import key
from utils.data_utils import get_cur_workspace, get_columns
from utils.print_utils import clear
from utils.storage import Storage
from render.column_manager import ColumnManager


class EventLoop:
    def __init__(self, storage_path):
        '''
            load from storage
            select last workspace
            create columns
        '''

        self.storage = Storage(storage_path)

        ws = get_cur_workspace(self.storage.data)
        num_cols = get_columns(ws)

        self.cm = ColumnManager()
        self.cm.init_data(ws)

    def _get_valid_key(self):
        valid_keys = [Key.up, Key.down, Key.left,
                      Key.right, key('q')]

        with Events() as events:
            while True:
                event = events.get()
                if event.key in valid_keys:
                    return event.key

    def loop(self):
        clear()
        user_input = ''
        while user_input != key('q'):
            self.cm.update(user_input)
            # self.cm.log()
            self.cm.render()
            user_input = self._get_valid_key()
            sleep(0.1)
            clear()
