import os
from Terminal.Colors import Colors

class Terminal:
    def __init__(self):
        self.width = os.get_terminal_size().columns
        self.height = 30
        self.colors = Colors

    def write(self, text, color=None):
        if color is None:
            color = self.colors.ENDC

        print(f"{color}{text}{self.colors.ENDC}")

