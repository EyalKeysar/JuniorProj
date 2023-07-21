import tkinter as tk
from client.GUI.windows.SignInConstants import *
from client.GameConstants import *
from client.GUI.windows.login_window import LoginWindow
from client.GUI.windows.register_window import RegisterWindow
from client.GUI.windows.main_window import MainWindow
import time
import threading
from client.logger import Logger
import sys


from shared.ServerAPI.serverapi import ServerAPI 

def main_screen():
    root = tk.Tk()
    root.withdraw() # hide the main window
    main_window = MainWindow(root) # show the main window

    logger = Logger()

    serverAPI = ServerAPI(logger)

    root.after(100, ServerAPI.Build)

    root.mainloop()
    sys.exit()

def update(root, serverAPI):
    
    update_status_bar(serverAPI.CheckConnection())

    root.after(100, update, root, serverAPI)

def update_status_bar(main_window, is_connected):
    main_window.connection_status_label.color = "#00FF00" if is_connected else "#FF0000"


if __name__ == "__main__":
    main_screen()
