import tkinter


class Settings():
    def __init__(self, root):
        self.root = root
        self.root.title("Economics Simulator")  # title at top of screen
        self.root.geometry("1280x720+100+50")  # resolution and centering
        self.root.resizable(False, False)  # does not allow for resizing
