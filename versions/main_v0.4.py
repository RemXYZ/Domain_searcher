import keyboard as keyb
# pip install keyboard
from colorama import Fore, Back, Style, init
# pip install colorama
init()
import os
import time
import re

""" 
pip install pyinstaller
to install ability .exe file

pyinstaller main.py
to create .exe file
run it in dist dirictory
"""

# domain_name = "azixon.com"
# text = os.popen("nslookup -type=A " + domain_name).read()
# print(text)
# sp = text.split("Addresses:  ")
# #lol = re.split(r"\n[\n\t]? *",sp[1])
# #lol.pop()
# sp2 = re.search(r"Address:( ){2}\d+.\d+.\d+.\d+", text)
# m = re.search(rf"{domain_name}", text)
# print("--------")
# print(sp)
# #print(lol)
# print(sp2)
# print(m)
#
#
# exit()


def close_prog():
    if keyb.is_pressed("esc"):
        os.system("cls")
        return 1
    return 0


def clear_console():
    os.system("cls")


#Yes, this is a workaround for which I am ashamed
def clear_cmd_input(release_key = None):
    keyb.send("esc")
    keyb.press("enter")
    input()
    keyb.release("enter")

    # if release_key is not None:
    #     time.sleep(0.01)
    #     keyb.release(release_key)


class Arrows_keys:

    def __init__(self):
        self.lol = 0


    def up(self):
        if keyb.is_pressed("up"):
            clear_cmd_input()
            return 1
        return 0


    def down(self):
        if keyb.is_pressed("down"):
            clear_cmd_input()
            return 1
        return 0




class Domain_zone_manip():
    def __init__(self):
        self.domain_zone = [".com", ".org", ".net"]
        self.selector = 0
        self.selected_domain = self.domain_zone[self.selector]
        self.selector_mode = 1


    def select(self, arrow_key):
        if arrow_key == "up":
            self.selector -= 1
        if arrow_key == "down":
            self.selector += 1

        # check for selector
        if self.selector < 0:
            self.selector = 0
        if self.selector >= len(self.domain_zone) - 1:
            self.selector = len(self.domain_zone) - 1

        self.print_domains_zone()


    def print_domains_zone(self):
        # print part #
        clear_console()
        print("Press Esc to exit,\nChoose with enter\nScroll the domain zone with arrows:\n")
        #print("Choose a domain zone:")
        for i, v in enumerate(self.domain_zone):
            highlighter = ""
            if self.selector == i:
                highlighter = Fore.RED + Back.WHITE

            print(" "+highlighter + v, end="")
            print(Style.RESET_ALL)


    def choose_domain_zone(self):
        if keyb.is_pressed("enter"):
            clear_console()
            self.selected_domain = self.domain_zone[self.selector]
            self.selector_mode = 0
            return 1
        return 0

    def get_domain_zone(self):
        return self.selected_domain


    def get_sts(self):
        return self.selector_mode




class Domain_manip():
    def __init__(self):
        self.domain_zone = ""
        self.searched_domain = ""


    def set_domain_zone(self, d_zone):
        self.domain_zone = d_zone


    def is_domain_exist(self, request):
        #my_ip = re.search(r"Address:( ){2}\d+.\d+.\d+.\d+", text)
        mth = re.search(rf"{self.searched_domain}", request)
        if mth is not None:
            sp = request.split("Addresses:  ")
            if len(sp) <= 1:
                return "No adresses"
            adresses = re.split(r"\n[\n\t]? *", sp[1])
            adresses.pop()
            return adresses
        return 0


    def nslookup(self):
        di_stm = os.popen("nslookup -type=A " + self.searched_domain + self.domain_zone).read()
        return di_stm



    def print_subdomain_input(self):
        clear_console()
        print("Write 'exit' to close program\nInput subdomain *" + self.domain_zone+" (without "+self.domain_zone+")")
        while self.searched_domain == "":
            self.searched_domain = input()
        # dominant statement
        di_stm = self.nslookup()
        adresses = self.is_domain_exist(di_stm)
        if adresses != 0:
            print(f"Domain {self.searched_domain}{self.domain_zone} already exists! \nIP adresses: {adresses}")
        else:
            print(f"Domain {self.searched_domain}{self.domain_zone} is free!")
        print()
        self.searched_domain = input("Write next domain:\n")
        if self.searched_domain == "exit":
            return "exit"



with open("motivation.txt", "r+") as f:
    # opening the file in read mode
    replacement = ""
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        changes = line.replace("hardships", "situations")
        # replacement = replacement + changes + "\n"

    # f.seek(0)
    # f.write(replacement)
    # f.truncate()



############# MAIN #############

#if __name__ == '__main__':

i = 0
arrows = Arrows_keys()

di_z = Domain_zone_manip()
di_z.print_domains_zone()

di = Domain_manip()


loop_time = 0.1

# render while loop
while 1:
    #i += 1
    time.sleep(loop_time)
    if close_prog():
        break

    if di_z.get_sts() == 1:
        aup = arrows.up()
        adown = arrows.down()

        if aup == 1:
            di_z.select("up")
        if adown == 1:
            di_z.select("down")

        if di_z.choose_domain_zone() == 1:
            di.set_domain_zone(di_z.get_domain_zone())
    else:
        di_sts = di.print_subdomain_input()
        if di_sts == "exit":
            break




