from colorama import Fore, Back, Style, init


def highlight(text: str, color, bg, reset = None):
    highlighter = ""
    #getattr(Fore, "RED") + getattr(Back, "WHITE")
    highlighter = getattr(Fore, color) + getattr(Back, bg)
    text = highlighter + text
    if reset is not None:
        text += Style.RESET_ALL
    return text


def reset_highliter():
    return Style.RESET_ALL



class Selector:
    def __init__(self, buttons = None):
        if buttons is None:
            buttons = []
        self.buttons = buttons
        self.buttons_len = 0
        self.selected = 0
        self.events = {}

    def i(self):
        return self.selected

    def v(self):
        return self.buttons[self.selected]

    def shift(self, key, callback = None):
        if key == "up":
            self.selected -= 1
        if key == "down":
            self.selected += 1

        if key == "left":
            self.selected -= 1
        if key == "right":
            self.selected += 1

        # check for selector
        if self.selected < 0:
            self.selected = self.buttons_len - 1
            # self.selected = 0
        if self.selected >= self.buttons_len:
            self.selected = 0
            # self.selected = self.buttons_len - 1

        if callback is not None:
            callback(self.selected)

    def run_event(self, name = None):
        if self.selected in self.events:
            if name is not None:
                return self.events[name]()
            return self.events[self.selected]()
        else:
            return None

    def set_event(self, i, callback):
        self.events[i] = callback

    def set_buttons(self, buttons: list):
        self.buttons = buttons
        self.buttons_len = len(self.buttons)


class GUI_selector(Selector):
    def __init__(self, buttons = None):
        if buttons is None:
            buttons = []
        super().__init__(buttons)
        self.color = "RED"
        self.bg = "WHITE"

    def set_color(self, color = "RED", bg = "WHITE"):
        self.color = color
        self.bg = bg


    def print(self):
        for i, v in enumerate(self.buttons):
            if self.selected == i:
                # highlight is a color
                print("·" + highlight(v, self.color, self.bg), end=reset_highliter()+"\n")
            else:
                print(" " + v)






