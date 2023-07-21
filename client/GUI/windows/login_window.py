import tkinter as tk
from client.GameConstants import *
from client.GUI.windows.SignInConstants import *

class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(f"{LOGIN_WINDOW_WIDTH}x{LOGIN_WINDOW_HEIGHT}")
        self.title("Login")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        self.logged_in = False
        self.username = ""
        self.password = ""

        self.username_label = tk.Label(self, text="Username", font=LOGIN_TXT_FONT)
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
    
        if(self.check_login(username, password)):
            print("Login successful")
            self.username = username
            self.password = password
            self.logged_in = True
        else:
            print("Login failed")

        self.destroy()

    def check_login(self, username, password):
        try:
            with open(PATH_TO_DB) as f:
                for line in f:
                    cur_user = line.split(";")[0]
                    cur_pass = line.split(";")[1]
                    print(f"cur_user: {cur_user}\ncur_pass: {cur_pass}")
                    if(username == cur_user and password == cur_pass):
                        f.close()
                        return True
            f.close()
            return False
        except Exception as e:
            print(e)
            return False
        