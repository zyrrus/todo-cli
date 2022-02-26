from utilities.print_utils import clear


class EventLoop:
    def __init__(self, storage_path):
        '''
            load from storage
            select last workspace
            create columns
        '''

        self.storage = Storage(path)
        self.cm = ColumnManager(self.storage.data)

    def loop(self):
        user_input = ''
        while user_input != ':q':
            clear()
            self.cm.render()
            user_input = input()
