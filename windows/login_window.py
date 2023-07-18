import tkinter as tk
from GameConstants import *
from SignInConstants import *

class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(f"{LOGIN_WINDOW_WIDTH}x{LOGIN_WINDOW_HEIGHT}")
        self.title("Login")
        self.resizable(False, False)

        self.username_label = tk.Label(self, text="username", font=LOGIN_TXT_FONT)
        self.username_entry = tk.Entry(self, width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.password_label = tk.Label(self, text="Password", font=LOGIN_TXT_FONT)
        self.password_entry = tk.Entry(self, show="●", width=LOGIN_TXT_INPUT_WIDTH, font=LOGIN_TXT_FONT)
        self.login_button = tk.Button(self, text="Login", command=self.login)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Perform login logic here
        print("Username:", username)
        print("Password:", password)
        self.destroy()