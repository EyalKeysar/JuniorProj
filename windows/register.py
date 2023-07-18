from collections.abc import Callable, Sequence
import tkinter as tk
from typing import Any
from GameConstants import *
from SignInConstants import *
from screen import Screen

class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(f"{REGISTER_WINDOW_WIDTH}x{REGISTER_WINDOW_HEIGHT}")
        self.title("Login")
        self.resizable(False, False)
        
        self.username_label = tk.Label(self, text="username", font=LOGIN_TXT_FONT)
        self.username_entry = tk.Entry(self, width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.password_label = tk.Label(self, text="Password", font=LOGIN_TXT_FONT)
        self.password_entry = tk.Entry(self, show="●", width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.password_confirm_label = tk.Label(self, text="Confirm Password", font=LOGIN_TXT_FONT)
        self.password_confirm_entry = tk.Entry(self, show="●", width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.register_button = tk.Button(self, text="Register", command=self.register)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.password_confirm_label.pack()
        self.password_confirm_entry.pack()
        self.register_button.pack()



    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_confirm_entry.get()
        # Perform login logic here
        print("Username:", username)
        print("Password:", password)
        print("Password Confirm:", password_confirm)
        self.destroy()