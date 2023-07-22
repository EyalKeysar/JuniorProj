import sys
import threading
import time

import tkinter as tk

from client.GUI.windows.windsows_constants import *
from client.GameConstants import *
from client.GUI.windows.login_window import LoginWindow
from client.GUI.windows.register_window import RegisterWindow
from client.GUI.windows.main_window import MainWindow
from client.GUI.windows.lobby_window import LobbyWindow
from client.window_handler import WindowHandler

from shared.logger import Logger
from shared.ServerAPI.server_api import ServerAPI 



def update(root, window_manager, serverAPI):

    # if the server is not connected, change the window to the main window
    if(not serverAPI.CheckConnection()):
        if(type(window_manager.GetCurWindow()) != MainWindow):
            window_manager.ChangeWindow(MainWindow)
    

    root.after(100, update, root, window_manager, serverAPI)

    

def update_status_bar(root, window_handler, serverAPI):
    window_handler.GetCurWindow().connection_status_label.config(
        bg="#00FF00" if serverAPI.GetConnectionStatus() else "#FF0000", 
        text="Connected" if serverAPI.GetConnectionStatus() else "Disconnected"
        )
    window_handler.GetCurWindow().connection_status_label.update()

    root.after(100, update_status_bar, root, window_handler, serverAPI)


def run():
    root = tk.Tk()
    root.withdraw() # hide the main window
    window_handler = WindowHandler(root) # create the window handler
    window_handler.ChangeWindow(MainWindow) # show the main window

    logger = Logger()

    serverAPI = ServerAPI(logger)

    root.after(100, serverAPI.Build)
    root.after(300, update, root, window_handler, serverAPI)
    root.after(400, update_status_bar, root, window_handler, serverAPI)

    root.mainloop()
    
    sys.exit()


if __name__ == "__main__":
    run()
