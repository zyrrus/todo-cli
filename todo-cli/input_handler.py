from pynput import keyboard
from pynput.keyboard import Key


class InputActions:
    def __init__(self, workspace, input_handler):
        self.ih = input_handler
        self.ws = workspace

    def rename_workspace(self):
        self.ih.start_textinput_mode()

    def rename_list(self):
        pass

    def rename_task(self):
        pass


class InputHandler:
    def __init__(self, workspace=None):
        self.ia = InputActions(workspace, self)
        self.key_map = {
            'w': self.ia.rename_workspace,
        }

    def _start_listener(self, on_press, on_release):
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

    def start_interactive_mode(self):
        def on_press(key):
            if key.char in self.key_map:
                self.key_map[key.char]()
            else:
                print(f'key {type(key)} {key} pressed')
            # try:
            #     # if key == 'a':
            #     print(f'alphanumeric key {key.char} pressed')
            # except AttributeError:
            #     # if key == key.up
            #     print(f'special key {key} pressed')

        def on_release(key):
            text_input_keys = ['w']
            if key == Key.esc or key in text_input_keys:
                return False

        self._start_listener(on_press, on_release)

    def start_textinput_mode(self, prompt="> "):
        text_input = input(prompt)
        return text_input.strip()


if __name__ == '__main__':
    ih = InputHandler()
    ih.start_interactive_mode()
