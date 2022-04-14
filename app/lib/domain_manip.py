import re
import os
import whois
import time
import json

from lib.console_win import close_prog, clear_console, clear_cmd_input
from lib.keyb_selector import Selector, GUI_selector, highlight, reset_highliter
from lib.file_management import File_base as File_base


# pip install python-whois
# more info:
# https://www.thepythoncode.com/article/extracting-domain-name-information-in-python


class Domain_manip:
    def __init__(self):
        self.domain_zone = ""
        self.searched_domain = ""
        self.status = 0
        self.first_start = 1
        self.f_inf = File_base()

    def is_domain_exist(self, request):
        # my_ip = re.search(r"Address:( ){2}\d+.\d+.\d+.\d+", text)
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

    # source: https://www.thepythoncode.com/article/extracting-domain-name-information-in-python
    def is_registered(self):
        domain_name = self.searched_domain + self.domain_zone
        """
        A function that returns a boolean indicating
        whether a `domain_name` is registered
        """
        try:
            w = whois.whois(domain_name)
        except Exception:
            return False
        else:
            self.registrar = w.registrar
            self.whois_server = w.whois_server
            self.creation_date = w.creation_date
            self.expiration_date = w.expiration_date
            return w

    # end of source

    def append_to_storage(self, data_arg, table = None):
        data = data_arg.copy()

        f_inf = self.f_inf
        path_main = f_inf.get_existing_path()

        columns = f_inf.get_exising_col()
        if table == "free":
            path_main = f_inf.get_free_path()
            columns = f_inf.get_free_col()
        if table == "favorite":
            path_main = f_inf.get_favorite_path()
            columns = f_inf.get_favorite_col()

        path, conf_path = path_main["storage"], path_main["conf"]
        conf = ""
        # MODIFY CONFIGURATION FILE
        with open("/".join(conf_path), "r") as f:
            conf = json.load(f)
            conf["auto_increment"] += 1

        # because there are anywhere id on begining
        data.insert(0, str(conf["auto_increment"]))

        # APPEND TO STORAGE
        with open("/".join(path), "a") as f:
            data_out = '"' + '","'.join(data) + '"\n'
            f.write(data_out)

        # MODIFY CONFIGURATION
        with open("/".join(conf_path), "w") as f:
            for i in range(len(data)):
                if data[i] == "Null":
                    continue
                loc_max = len(data[i])

                if conf[columns[i] + "_max"] < loc_max:
                    if loc_max > 30:
                        conf[columns[i] + "_max"] = 30
                    else:
                        conf[columns[i] + "_max"] = loc_max

            json.dump(conf, f)



    #
    def event_handler(self, option, data=None):
        if self.searched_domain == "0":
            return "exit"
        if self.searched_domain == "<-":
            self.searched_domain = ""
            self.set_sts(0)
            return "return"
        return None

    #
    def subdomain_input(self):
        clear_console()
        print(
            "Write '0' to close program"
            "\n      '1' to add domain to favorites"
            "\n      '<-' to return selecting domain zone"
            "\nInput domain name: *" + self.domain_zone + " (without " + self.domain_zone + ")")
        if self.searched_domain == "":
            self.searched_domain = input("\nWrite domain name:\n")
            if self.searched_domain == "":
                return None

            event = self.event_handler(self)
            if event is not None: return event

        # dominant statement
        whois_info = self.is_registered()
        if whois_info != 0:
            exp_date = whois_info.expiration_date
            if type(exp_date) == list:
                exp_date = exp_date[0]
            cr_date = whois_info.creation_date
            if type(cr_date) == list:
                cr_date = cr_date[0]

            print(f"\nDomain {self.searched_domain}{self.domain_zone} "
                  f"already {highlight('exists', 'WHITE', 'RED', 1)} ! "
                  f"\nRegistrar: {whois_info.registrar}"
                  f"\nServer: {whois_info.whois_server}"
                  f"\nExpiration date: {exp_date}"
                  f"\nCreation date: {cr_date}"
                  )

            data_in = [
                self.searched_domain + self.domain_zone,
                time.strftime('%Y-%m-%d %H:%M:%S'),
                whois_info.registrar,
                str(exp_date),
                str(cr_date)
            ]

            self.append_to_storage(data_in, "existing")
        else:
            print(f"\nDomain {self.searched_domain}{self.domain_zone} is "
                  f"{highlight('free', 'WHITE', 'GREEN', 1)} !")

            data_in = [
                self.searched_domain + self.domain_zone,
                time.strftime('%Y-%m-%d %H:%M:%S')
            ]
            self.append_to_storage(data_in, "free")
        print()

        last_domain_name = self.searched_domain
        self.searched_domain = input("Write next domain:\n")
        event = self.event_handler(self)
        if event is not None: return event

        # appending to favorite
        if self.searched_domain == "1":

            if whois_info == 0:
                data_in.append("Null")
                data_in.append("Null")
                data_in.append("Null")

            self.append_to_storage(data_in, "favorite")
            self.searched_domain = ""

    def set_domain_zone(self, d_zone):
        self.domain_zone = d_zone

    def set_sts(self, b, not_first=None):
        self.status = b
        if not_first is None:
            self.first_start = b

    def set_first_start(self, b):
        self.first_start = b

    def get_first_start(self):
        return self.first_start

    def get_sts(self):
        return self.status
