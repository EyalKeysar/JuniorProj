import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
Config.set('kivy', 'window_icon', './Assets/game_icon.png') 

import sys
import os
from multiprocessing import Process
import time
import socket
from GameConstants import *
from Network.constants import *
from game import Game
from networks import *
from logger import Logger
from signinapp import SignInApp


def main():
    logger =  Logger() 
    logger.log(" * Starting game")
    

    # client_socket = CreateSocket(logger)
    # logger.log("Connected to server")

    is_connected = True

    # p1 = Process(target=main_loop, args=(logger, client_socket, is_connected))
    # p1.start()
    
    SignInApp(logger).run()
    logger.log(" * Game ended")


if __name__ == "__main__":
    main()