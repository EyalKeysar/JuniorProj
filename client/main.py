import sys
import threading
import time

import tkinter as tk

from client.GUI.windows.SignInConstants import *
from client.GameConstants import *
from client.GUI.windows.login_window import LoginWindow
from client.GUI.windows.register_window import RegisterWindow
from client.GUI.windows.main_window import MainWindow

from shared.logger import Logger
from shared.ServerAPI.serverapi import ServerAPI 



def update(root, serverAPI):
    
    serverAPI.CheckConnection()

    root.after(100, update, root, serverAPI)

def update_status_bar(root, main_window, serverAPI):
    main_window.connection_status_label.config(
        bg="#00FF00" if serverAPI.GetConnectionStatus() else "#FF0000", 
        text="Connected" if serverAPI.GetConnectionStatus() else "Disconnected"
        )
    main_window.connection_status_label.update()

    root.after(100, update_status_bar, root, main_window, serverAPI)


def run():
    root = tk.Tk()
    root.withdraw() # hide the main window
    main_window = MainWindow(root) # show the main window

    logger = Logger()

    serverAPI = ServerAPI(logger)

    root.after(100, serverAPI.Build)
    root.after(300, update, root, serverAPI)
    root.after(400, update_status_bar, root, main_window, serverAPI)

    root.mainloop()
    
    sys.exit()


if __name__ == "__main__":
    run()
