from os import system as os_system


class Window():
    def __init__(self):
        ### window size is in symbols size ###
        self.win_width = 90
        self.win_height = 20
        self.render_time = 0.08

        ### frame PART ###
        self.text_position = {
            "y": ["top", "bottom", "center"],
            "x": ["left", "right", "center"]
        }
        self.align_y = {
            "x": "left",
            "y": "top"
        }
        self.print_space = []

    def get_render_time(self):
        return self.render_time

    def set_render_time(self, time):
        self.render_time = time

    def resize(self):
        os_system(f'mode con: cols={self.win_width} lines={self.win_height}')

    def cons_prepare(self, clear=1, align: dict = None):
        if align is None:
            align = {
                "x": "left",
                "y": "top"
            }

        self.align_y = align

        if clear == 1:
            self.print_space.clear()

    def prt(self, text, align: dict = None, end="\n"):
        if align is None:
            align = {"x": "left"}

        spl_t = str(text).split("\n")
        # print({text})
        if end == "" and len(self.print_space) != 0:
            self.print_space[len(self.print_space) - 1]["text"] = self.print_space[len(self.print_space) - 1][
                                                                      "text"] + str(text)
            return

        for t in spl_t:
            self.print_space.append({
                "text": str(t) + str(end),
                "align": align
            })

    def set_position(self, i):
        print(self.print_space)
        # if self.print_space[i]["align"]:

    def print_frame(self):
        # clear_console()
        to_print = self.print_space
        text_len = len(to_print)
        text_i = 0
        start_point = 0
        win_height = self.win_height - 1
        win_width = self.win_width
        paragraph_align = self.align_y
        ### center
        if paragraph_align["y"] == self.text_position["y"][2]:
            start_point = (win_height - text_len) // 2
        ### bottom
        if paragraph_align["y"] == self.text_position["y"][1]:
            start_point = win_height - text_len

        for i in range(win_height):
            if i == start_point and text_i < text_len:
                if paragraph_align["x"] == self.text_position["y"][2]:
                    t_space = (win_width - len(to_print[text_i]["text"])) // 2
                    for sp in range(t_space):
                        print(" ", end="")
                print(to_print[text_i]["text"], end="")
                text_i += 1
                start_point += 1
            else:
                print("")