from keyboard import is_pressed, send, press, release
from os import system as os_system
#from lib.current_window import Current_window


def close_prog():
    if is_pressed("esc"):
        os_system("cls")
        return 1
    return 0


def clear_console():
    os_system("cls")


# Yes, this is a workaround for which I am ashamed
def clear_cmd_input(reset_pos=None, only_cmd=None):
    # if only_cmd == 1:
    #     if Current_window() == "cmd.exe":
    #         return

    send("esc")
    if reset_pos == 1:
        press("enter")
        input()
        release("enter")
