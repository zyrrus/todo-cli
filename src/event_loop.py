from time import sleep

from pynput.keyboard import Events

from constants import Keys
from utils.data_utils import get_cur_workspace, get_columns
from utils.print_utils import clear
from utils.storage import Storage
from render.column_manager import ColumnManager


class EventLoop:
    def __init__(self, storage_path):
        self.storage = Storage(storage_path)

        ws = get_cur_workspace(self.storage.data)
        num_cols = get_columns(ws)

        self.cm = ColumnManager()
        self.cm.init_data(ws)

    def _get_valid_key(self):
        with Events() as events:
            while True:
                event = events.get()
                if Keys.is_valid(event.key):
                    return event.key

    def loop(self):
        clear()
        user_input = ''
        while not Keys.is_equal(user_input, Keys.leave):
            self.cm.update(user_input)
            # self.cm.log()
            self.cm.render()
            user_input = self._get_valid_key()
            sleep(0.12)
            clear()
