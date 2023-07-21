import tkinter as tk
from client.GameConstants import *
from client.GUI.windows.SignInConstants import *
from client.GUI.windows.login_window import LoginWindow
from client.GUI.windows.register_window import RegisterWindow


class MainWindow(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.title(GAME_NAME)
        self.resizable(False, False)

        self.connection_status_label = tk.Label(self, text="Disconnected", bg="#FF0000", width=SCREEN_WIDTH, height=CONNECTIONSTATUSBARHEIGHT)
        self.title_label = tk.Label(self, text = SIGNINTITLETXT, bg = TITLEBGCLR, width=SCREEN_WIDTH, height=SIGNINTITLETXTHEIGHT, font = SIGNINTXTFONT)
        self.login_button = tk.Button(self, text = "Login", command=lambda: LoginWindow(parent), font=BTNFONT, bg=BTNBGCLR, width=SIGNINBUTTONWIDTH, height=SIGNINBUTTONHEIGHT, activebackground=BTNCLR_ON_CLICK)
        self.register_button = tk.Button(self, text = "Register",command=lambda: RegisterWindow(parent) , font=BTNFONT, bg=BTNBGCLR, width=SIGNINBUTTONWIDTH, height=SIGNINBUTTONHEIGHT, activebackground=BTNCLR_ON_CLICK)

        self.connection_status_label.pack()
        self.title_label.pack()
        self.login_button.pack()
        self.register_button.pack()
        

