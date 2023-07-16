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
from network_handler import NetworkHandler


def main():
    logger =  Logger() 
    logger.log(" * Starting game")
    
    SignInApp().run()
    logger.log(" * Game ended")


if __name__ == "__main__":
    main()