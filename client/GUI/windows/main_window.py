import tkinter as tk
from client.GameConstants import *
from client.GUI.windows.windsows_constants import *
from client.GUI.windows.login_window import LoginWindow
from client.GUI.windows.register_window import RegisterWindow


class MainWindow(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.title(GAME_NAME)
        self.resizable(False, False)

        self.connection_status_label = tk.Label(
            self, text="Disconnected", bg="#FF0000", font=CONNECTION_STATUS_BAR_TXT_FONT, width=SCREEN_WIDTH, height=CONNECTION_STATUS_BAR_HEIGHT)
        
        self.title_label = tk.Label(
            self, text = SIGN_IN_TITLE_TXT, bg = TITLE_BG_CLR, width=SCREEN_WIDTH, height=SIGN_IN_TITLE_HEIGHT, font = TITLE_TXT_FONT)
        
        self.login_button = tk.Button(
            self, text = "Login", command=lambda: LoginWindow(parent), font=BTN_FONT, bg=BTN_BG_CLR, width=BTN_WIDTH, height=BTN_HEIGHT, activebackground=BTN_CLR_ON_CLICK)
        
        self.register_button = tk.Button(
            self, text = "Register",command=lambda: RegisterWindow(parent) , font=BTN_FONT, bg=BTN_BG_CLR, width=BTN_WIDTH, height=BTN_HEIGHT, activebackground=BTN_CLR_ON_CLICK)

        self.connection_status_label.pack()
        self.title_label.pack()
        self.login_button.pack()
        self.register_button.pack()
        

