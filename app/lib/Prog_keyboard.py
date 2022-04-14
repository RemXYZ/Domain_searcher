import keyboard as keyb
# pip install keyboard
from win32gui import GetWindowText, GetForegroundWindow

from lib.console_win import close_prog, clear_console, clear_cmd_input

class Prog_keyboard:
    def __init__(self):
        self.is_pressed_sts = 0
        self.key = " "
        self.my_window = ""

    def key_release(self):
        self.is_pressed_sts = 0

    def down(self):
        if self.is_pressed_sts == 1:
            self.is_pressed_sts = 0
            return 0
        key = keyb.read_key()

        if self.my_window != GetWindowText(GetForegroundWindow()):
            return 0
        clear_cmd_input()
        self.is_pressed_sts = 1
        self.key = key
        return 1

    def press_down(self):
        self.is_pressed_sts = 1
        key = keyb.read_key()
        clear_cmd_input()
        self.key = key
        self.is_pressed_sts = 0
        return key

    def is_pressed(self):
        key = self.get_key()
        if keyb.is_pressed(key) == 0:
            self.key_release()
        # print(keyb.is_pressed(key), self.is_pressed_sts)
        #return keyb.is_pressed(key)
        return self.is_pressed_sts

    def get_key(self):
        return self.key