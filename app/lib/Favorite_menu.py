from lib.file_management import Favorite_manager
from lib.console_win import close_prog, clear_console, clear_cmd_input


class Favorite_menu:
    def __init__(self):
        self.buttons = ["Select only domain name", "Select full information", "Exit"]
        self.selected = 0
        self.status = 0
        self.first_start = 1

        self.col = ["id", "domain_name", "time"]

    def get_domains(self):
        dm_mng = Favorite_manager()
        domains = dm_mng.select(self.col)

        return domains

    def print_menu(self):
        clear_console()
        print("Press \"`\" to return, \n"
              "      \"Esc\" to exit \n")

    def exit(self):
        self.set_sts(0)

    def show_col(self):
        pass

    def select_col(self, i):
        if i == 0:
            pass
        if i == 1:
            self.col += ["registrar", "expiration_date", "creation_date"]

    ### SETTERS
    def set_sts(self, b, not_first=None):
        self.status = b
        if not_first is None:
            self.first_start = b

    def set_first_start(self, b):
        self.first_start = b

    ### GETTERS
    def get_first_start(self):
        return self.first_start

    def get_sts(self):
        return self.status

    def get_buttons(self):
        return self.buttons