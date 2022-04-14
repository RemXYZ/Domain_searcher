from lib.console_win import close_prog, clear_console, clear_cmd_input

class Domain_zone_manip:
    def __init__(self):
        self.domain_zone = [".com", ".pl", ".ru", ".org", ".net", "<-"]
        self.selected = 0
        self.selected_domain = self.domain_zone[self.selected]
        self.status = 0
        self.first_start = 1

    def print_menu(self):
        # print part #
        clear_console()
        print("Choose a domain zone:\n")
        # print("Choose a domain zone:")


    def choose_domain_zone(self, key):
        if key == "enter":
            clear_console()
            self.status = 0
            if self.selected == len(self.domain_zone) - 1:
                return "return"
            self.selected_domain = self.domain_zone[self.selected]
            return 1
        return 0

    def set_selector(self, i):
        self.selected = i

    def set_sts(self, b, not_first = None):
        self.status = b
        if not_first is None:
            self.first_start = b

    def set_first_start(self, b):
        self.first_start = b

    def get_first_start(self):
        return self.first_start

    def get_domains(self):
        return self.domain_zone

    def get_domain_zone(self):
        return self.selected_domain

    def get_sts(self):
        return self.status