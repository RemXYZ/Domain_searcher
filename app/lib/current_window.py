import psutil
import ctypes
from ctypes import wintypes
from lib.my_algorythm import binary_search

# source: https://ru.stackoverflow.com/questions/1302716/%D0%9D%D0%B0%D0%B9%D1%82%D0%B8-%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BE%D0%BA%D0%BD%D0%B0-%D0%BF%D1%80%D0%B8-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D0%B8-python
# class Current_window:
#     def __init__(self):
#         pass


def current_window():
    pid = wintypes.DWORD()
    active = ctypes.windll.user32.GetForegroundWindow()
    active_window = ctypes.windll.user32.GetWindowThreadProcessId(active, ctypes.byref(pid))
    pid = pid.value

    processed = psutil.process_iter()
    list_pr = tuple(processed)
    exe = binary_search(list_pr, pid, lambda v: v.pid)
    if exe != 0:
        return list_pr[exe].name()
    return 0

    # for item in psutil.process_iter():
    #     if pid == item.pid:
    #         print(item.name())