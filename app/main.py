from colorama import Fore, Back, Style, init
# pip install colorama
init()

import os
import time

from win32gui import GetWindowText, GetForegroundWindow

# pip install pywin32
# pip install win32gui

""" 
pip install pyinstaller
to install ability .exe file

pyinstaller main.py
to create .exe file
run it in dist dirictory
"""

# my files
from lib.prog_window import Window
from lib.console_win import close_prog, clear_console, clear_cmd_input
from lib.keyb_selector import Selector, GUI_selector, highlight, reset_highliter
# from lib.current_window import current_window as current_window
from lib.Prog_keyboard import Prog_keyboard as Prog_keyboard

from lib.file_management import File_manager as File_manager

from lib.main_menu import Domain_menu
from lib.Domain_zone_manip import Domain_zone_manip as Domain_zone_manip
from lib.domain_manip import Domain_manip as Domain_manip
from lib.Favorite_menu import Favorite_menu



from lib.my_algorythm import binary_search, quicksort
###### GLOBALS VARIABLES ########

WIN = Window()

my_title = "Domain_searcher_cmd"
os.system("title " + my_title)

F_MNG = File_manager()

####### END OF GLOBALS ###########

####### TEST PART #########


# print (quicksort([76,3,4,7,3,2,1,56,54,1,6]))
#
#
# out_data = {
#     "auto_increment": 0,
#     "domain_dict": {}
# }
# dict_start = ord("a")
# for i in range(10+26):
#     if i < 10:
#         out_data["domain_dict"][i] = []
#         continue
#     out_data["domain_dict"][chr(dict_start)] = []
#     dict_start += 1
#
# dm_dict = out_data["domain_dict"].keys()
# out_data["domain_dict"]["a"].append(12)
# out_data["domain_dict"]["a"].append(55)
# out_data["domain_dict"]["a"].append(23)
#
# abc_dict = tuple(dm_dict)
# abc = binary_search(abc_dict, ord("a"), lambda x: ord(str(x)))
# v = abc_dict[abc]
# print(out_data["domain_dict"][v])
#
# exit()

#### END OF TEST PART #####

# kb = Prog_keyboard()
# while 1:
#     time.sleep(0.04)
#     if kb.is_pressed() == 1:
#         continue
#     kb.down()
#     key = kb.get_key()
#     if key == "esc":
#         break
#     print(key)
#
# exit()

# with open("motivation.txt", "r+") as f:
#     # opening the file in read mode
#     replacement = ""
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         line = line.strip()
#         changes = line.replace("hardships", "situations")
#         # replacement = replacement + changes + "\n"
#
#     # f.seek(0)
#     # f.write(replacement)
#     # f.truncate()

############ MAIN PART ############

# if __name__ == '__main__':

i = 0
WIN.resize()
pkey = Prog_keyboard()
pkey.my_window = my_title

###### MAIN MENU #######
menu_s = GUI_selector()
menu = Domain_menu()
menu.set_sts(1)
menu_s.set_buttons(menu.get_buttons())
menu_s.set_color("BLACK")


###### FAVORITE MENU #####
fv = Favorite_menu()
fv_s = GUI_selector()
fv_s.set_buttons(fv.get_buttons())
fv_s.set_color("BLACK")

fv_dm = Favorite_menu()
fv_dm_s = GUI_selector()
fv_dm_s.set_color("BLACK")

###### DOMAIN ZONE SELECTOR ######
dmz_s = GUI_selector()

dmz = Domain_zone_manip()
dmz_s.set_buttons(dmz.get_domains())
# dmz.print_menu()

###### DOMAIN FINDER ######
dm = Domain_manip()

###### GENERAL ######
loop_time = 0.08


###### EVENT SETTING ON BUTTONS #######

def run_search_menu():
    menu.search()
    dmz.set_sts(1)


def run_fv_menu():
    menu.set_sts(0)
    fv.set_sts(1)


menu_s.set_event(0, run_search_menu)
menu_s.set_event(1, run_fv_menu)
menu_s.set_event(5, menu.exit)

###### RENDER WHILE LOOP #######
while 1:
    # i += 1
    time.sleep(loop_time)

    if my_title != GetWindowText(GetForegroundWindow()):
        continue

    if close_prog():
        break

    ###### SHOWING MAIN MENU PART #######

    if menu.get_sts() == 1:
        if menu.get_first_start() == 1:
            menu.set_first_start(0)
            menu.print_menu()
            menu_s.print()

        if pkey.is_pressed() == 1:
            continue
        if pkey.down() == 0:
            continue
        key = pkey.get_key()

        if key == "enter":
            option = menu_s.run_event()
            # option = menu.event_handler(menu_s.i())
            match option:
                case "exit":
                    break
            continue

        menu_s.shift(key)
        menu.print_menu()
        menu_s.print()

        continue
        # pass

    ###### SELECTING DOMAIN ZONE PART #######

    if dmz.get_sts() == 1:
        if dmz.get_first_start() == 1:
            dmz.set_first_start(0)
            dmz.print_menu()
            dmz_s.print()

        if pkey.is_pressed() == 1:
            continue
        pkey.down()
        key = pkey.get_key()

        dmz_s.shift(key)
        dmz.set_selector(dmz_s.i())

        dmz.print_menu()
        dmz_s.print()

        if dmz.choose_domain_zone(key) == 1:
            dm.set_domain_zone(dmz.get_domain_zone())
            dm.set_sts(1)
        if dmz.choose_domain_zone(key) == "return":
            menu.set_sts(1)

    ####### SHOWING DOMAIN INPUT PART ######

    if dm.get_sts() == 1:
        di_sts = dm.subdomain_input()
        match di_sts:
            case "return":
                dmz.set_sts(1)
                dmz.set_first_start(1)
            case "exit":
                break

    ###### SHOW FAVORITE PART #######


    if fv.get_sts() == 1:
        if fv.get_first_start() == 1:
            fv.set_first_start(0)
            fv.print_menu()

            domains = fv.get_domains()


            fv_s.set_event(0, lambda: fv_dm.select_col(0) and fv_dm.set_sts(1) and fv.set_sts(0))
            fv_s.set_event(1, lambda: fv_dm.select_col(1) and fv_dm.set_sts(1) and fv.set_sts(0))
            fv_s.set_event(2, lambda: menu.set_sts(1) and fv.set_sts(0))
            fv_s.print()

        if pkey.is_pressed() == 1:
            continue
        if pkey.down() == 0:
            continue
        key = pkey.get_key()
        fv_s.shift(key)

        fv.print_menu()
        fv_s.print()

        if key == "`":
            option = fv_s.run_event(2)

        if key == "enter":
            option = fv_s.run_event()


    # if fv_dm.get_sts() == 1:
    #     if fv_dm.get_first_start() == 1:
    #         fv_dm.set_first_start(0)
    #         fv_dm.print_menu()
    #         dms = fv.get_domains()
    #
    #         fv_dm_s.set_buttons(["exit"])
    #         fv_dm_s.set_event(0, lambda: menu.set_sts(1) and fv.set_sts(0))
    #         fv_dm_s.print()
    #
    #     if pkey.is_pressed() == 1:
    #         continue
    #     if pkey.down() == 0:
    #         continue
    #     key = pkey.get_key()
    #     fv_s.shift(key)
    #
    #     fv.print_menu()
    #     fv_s.print()
    #
    #     if key == "`":
    #         option = fv_s.run_event(1)
    #
    #     if key == "enter":
    #         option = fv_s.run_event()


clear_console()
