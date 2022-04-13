from lib.console_win import close_prog, clear_console, clear_cmd_input

class Domain_menu:
    def __init__(self):
        self.buttons = ["Search", "Favorites", "History", "Settings", "Help", "Exit"]
        self.selected = 0
        self.status = 1
        self.first_start = 1

    def print_menu(self):
        clear_console()
        print("Hi! Quick introduction:\n"
              "Press \"Esc\" to exit\n"
              "Use arrows, (\u2191 \u2193 \u2192 \u2190) to scroll\n"
              "Use \"Enter\" to choose option\n"
              )

    def search(self):
        self.set_sts(0)

    def exit(self):
        return "exit"

    # def event_handler(self, i):
    #     if i == 0:
    #         self.search()
    #         return "search"
    #     if i == 3:
    #         return "exit"
    #     print(self.buttons[i])

    def set_sts(self, b, not_first=None):
        self.status = b
        if not_first is None:
            self.first_start = b

    def set_first_start(self, b):
        self.first_start = b

    def get_first_start(self):
        return self.first_start

    def get_buttons(self):
        return self.buttons

    def get_sts(self):
        return self.status

