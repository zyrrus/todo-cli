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

    def loop(self):
        clear()
        user_input = ''
        while user_input != ':q':
            self.cm.render()
            user_input = input()
            clear()
