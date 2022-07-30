from models.abstract_panels import Panel, ParentPanel


class Workspace():
    def __init__(self, title="<new workspace>"):
        self.title = title

        self.lists = []
        self.selected_list_index = -1

        # TODO: implement viewing window
        self.view_size = 3
        self.view_range = (0, self.view_size)

    def __str__(self):
        ws = f"# {self.title}\n\n"
        ls = [str(child) for child in self.lists]
        return ws + "\n".join(ls)

    def rename(self, title):
        self.title = title

    def get_selected(self):
        return self.lists[self.selected_list_index]

    def select(self, new_selected_index):
        if new_selected_index >= len(self.lists):
            new_selected_index = 0
        if self.selected_list_index > -1:
            self.lists[self.selected_list_index].set_is_selected(False)
        self.lists[new_selected_index].set_is_selected(True)
        self.selected_list_index = new_selected_index
        return self.lists[self.selected_list_index]

    def add_child(self, ls):
        self.lists.insert(self.selected_list_index + 1, ls)
        self.select(self.selected_list_index + 1)

    def select_right(self):
        return self.select(self.selected_list_index + 1)

    def select_left(self):
        return self.select(self.selected_list_index - 1)

    def swap_right(self):
        if len(self.lists) < 2:
            return

        ls = self.lists
        l = self.selected_list_index
        r = (l + 1) % len(ls)

        ls[l], ls[r] = ls[r], ls[l]
        self.select_right()

    def swap_left(self):
        if len(self.lists) < 2:
            return

        ls = self.lists
        r = self.selected_list_index
        l = r - 1
        if l < 0:
            l += len(ls)

        ls[l], ls[r] = ls[r], ls[l]
        self.select_left()


class List():
    def __init__(self, title="<new list>"):
        self.title = title
        self.is_selected = False

        self.tasks = []
        self.selected_task_index = -1

        # TODO: implement viewing window
        self.view_size = 5
        self.view_range = (0, self.view_size)

    def __str__(self):
        prefix = "> " if self.is_selected else ""
        ls = f"\n{prefix}## {self.title}\n\n"
        ts = [str(child) for child in self.tasks]
        return ls + "\n".join(ts)

    def rename(self, title):
        self.title = title

    def get_selected(self):
        return self.tasks[self.selected_task_index]

    def set_is_selected(self, is_selected):
        if self.selected_task_index < 0:
            return

        self.tasks[self.selected_task_index].set_is_selected(is_selected)
        self.is_selected = is_selected

    def select(self, new_selected_index):
        if new_selected_index >= len(self.tasks):
            new_selected_index = 0
        if self.selected_task_index > -1:
            self.tasks[self.selected_task_index].set_is_selected(False)
        self.tasks[new_selected_index].set_is_selected(True)
        self.selected_task_index = new_selected_index
        return self.tasks[self.selected_task_index]

    def add_child(self, ts):
        self.tasks.insert(self.selected_task_index + 1, ts)
        self.selected_task_index += 1

    def select_down(self):
        return self.select(self.selected_task_index + 1)

    def select_up(self):
        return self.select(self.selected_task_index - 1)

    def select_right(self): pass

    def select_left(self): pass

    def swap_down(self):
        if len(self.tasks) < 2:
            return

        ts = self.tasks
        u = self.selected_list_index
        d = (u + 1) % len(ts)

        ls[u], ls[d] = ls[d], ls[u]
        self.select_down()

    def swap_up(self):
        if len(self.tasks) < 2:
            return

        ts = self.tasks
        d = self.selected_list_index
        u = d - 1
        if u < 0:
            u += len(ts)

        ls[u], ls[d] = ls[d], ls[u]
        self.select_up()


class Task():
    def __init__(self, title="<new task>"):
        self.title = title
        self.is_selected = False

    def __str__(self):
        prefix = ">> " if self.is_selected else ""
        return f"{prefix}- {self.title}"

    def set_is_selected(self, is_selected):
        self.is_selected = is_selected

    def rename(self, title):
        self.title = title
