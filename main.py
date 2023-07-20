import tkinter as tk
from SignInConstants import *
from GameConstants import *
from windows.login_window import LoginWindow
from windows.register_window import RegisterWindow
from windows.main_window import MainWindow
import time
import threading
from logger import Logger
from network_handler import NetworkHandler


def main_screen():
    root = tk.Tk()
    root.withdraw() # hide the main window
    main_window = MainWindow(root) # show the main window

    logger = Logger()
    network_handler = NetworkHandler(logger)

    root.after(100, network_check, root, network_handler)
    root.after(1000, update_connection_status, root, main_window, network_handler)

    root.mainloop()
    
def update_connection_status(root, main_window, network_handler):
    if(network_handler.connection_status):
        main_window.connection_status_label.config(text="Connected", bg="#00FF00")
    else:
        main_window.connection_status_label.config(text="Disconnected", bg="#FF0000")
    root.after(1000, update_connection_status, root, main_window, network_handler)

def network_check(root, network_handler):
    network_handler.CheckConnection()
    root.after(100, network_check, root, network_handler)



if __name__ == "__main__":
    main_screen()

"""


"""