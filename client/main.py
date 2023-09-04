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

from client.Game.game import Game

from shared.logger import Logger
from shared.ServerAPI.server_api import ServerAPI 
from shared.debug import *

def periodic_function(func, root):
    def wrapper(*args, **kwargs):
        
        func(*args, **kwargs)

    return wrapper

def update(root, window_manager, serverAPI):

    # if the server is not connected, change the window to the main window

    # if(not serverAPI.CheckConnection()):
    #     if(type(window_manager.GetCurWindow()) != MainWindow):
    #         window_manager.ChangeWindow(MainWindow)
    
    serverAPI.CheckConnection()

    time.sleep(1)
    root.after(100, update, root, window_manager, serverAPI)

    

def update_status_bar(root, window_handler, serverAPI):
    window_handler.GetCurWindow().connection_status_label.config(
        bg= STATUS_BAR_CONNECT_CLR if serverAPI.GetConnectionStatus() else STATUS_BAR_DISCONNECT_CLR, 
        text= STATUS_BAR_CONNECT_TXT if serverAPI.GetConnectionStatus() else STATUS_BAR_DISCONNECT_TXT
        )
    window_handler.GetCurWindow().connection_status_label.update()

    root.after(100, update_status_bar, root, window_handler, serverAPI)


def run():
    root = tk.Tk()
    root.withdraw() # hide the main window
    window_handler = WindowHandler(root) # create the window handler


    logger = Logger()

    serverAPI = ServerAPI(logger)


    window_handler.ChangeWindow(MainWindow, window_handler, serverAPI) # show the main window


    # game = Game(serverAPI)

    # game.run()

    root.after(10, serverAPI.Build)
    
    # root.after(200, game.run)
    root.after(300, update, root, None, serverAPI)
    # # root.after(150, update_status_bar, root, window_handler, serverAPI)

    root.mainloop()
    
    sys.exit()


if __name__ == "__main__":
    run()
