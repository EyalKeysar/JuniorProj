import tkinter as tk
from GameConstants import *

class TkScreen():
    def __init__(self, **kwargs):
        self.screen = tk.Tk()
        self.screen.resizable(False, False)
        self.screen.title(SCREEN_TITLE)
        # add kwargs as window children
        for key, value in kwargs.items():
            print(key, value)
            value.pack()

    def add_widget(self, widget):
        widget.pack()

    def start(self):
        self.screen.mainloop()

    def show_screen(self):
        self.screen.tkraise()
        for widget in self.screen.winfo_children():
            widget.pack()
        
    def clear_screen(self):
        for widget in self.screen.winfo_children():
            widget.destroy()