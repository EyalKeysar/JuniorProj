import tkinter as tk
from GameConstants import *

class Screen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.resizable(False, False)
        self.title(SCREEN_TITLE)

        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget)

    def remove_widget(self, widget):
        self.widgets.remove(widget)

    def show(self):
        for widget in self.widgets:
            if(isinstance(widget, tk.Button)):
                widget.pack(pady=10)
            else:
                widget.pack()

    def close(self):
        self.destroy()