import tkinter as tk
from client.GUI.windows.SignInConstants import *
from client.GameConstants import *
from client.GUI.windows.login_window import LoginWindow
from client.GUI.windows.register_window import RegisterWindow
from client.GUI.windows.main_window import MainWindow
import time
import threading
from shared.logger import Logger
import sys


from shared.ServerAPI.serverapi import ServerAPI 

def main_screen():
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

def update(root, serverAPI):
    serverAPI.CheckConnection()
    root.after(100, update, root, serverAPI)

def update_status_bar(root, main_window, serverAPI):
    print(serverAPI.GetConnectionStatus())
    main_window.connection_status_label.config(bg="#00FF00" if serverAPI.GetConnectionStatus() else "#FF0000")
    main_window.connection_status_label.config(text="Connected" if serverAPI.GetConnectionStatus() else "Disconnected")
    main_window.connection_status_label.update()
    main_window.update()
    root.after(100, update_status_bar, root, main_window, serverAPI)


if __name__ == "__main__":
    main_screen()
