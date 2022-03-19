from pynput.keyboard import Key, KeyCode, Listener
from pynput import keyboard


class InputManager:
    def __init__(self, hotkeys):
        self.hotkeys = hotkeys
        self._pressed_vks = set()

    def _get_vk(self, key):
        """
        Get the virtual key code from a key.
        These are used so case/shift modifications are ignored.
        """
        return key.vk if hasattr(key, 'vk') else key.value.vk

    def _is_combination_pressed(self, combination):
        """ Check if a combination is satisfied using the keys pressed in pressed_vks """
        return all([self._get_vk(key) in self._pressed_vks for key in combination])

    def _on_press(self, key):
        """ When a key is pressed """
        vk = self._get_vk(key)  # Get the key's vk
        # Add it to the set of currently pressed keys
        self._pressed_vks.add(vk)

        for combination in self.hotkeys:  # Loop through each combination
            # Check if all keys in the combination are pressed
            if self._is_combination_pressed(combination):
                # If so, execute the function
                self.hotkeys[combination]()

    def _on_release(self, key):
        """ When a key is released """
        vk = self._get_vk(key)  # Get the key's vk
        # Remove it from the set of currently pressed keys
        self._pressed_vks.remove(vk)

    def start(self):
        with Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            listener.join()
