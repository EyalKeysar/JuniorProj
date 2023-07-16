import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
Config.set('kivy', 'window_icon', './Assets/game_icon.png') 

from screens.signinscreen import SignInScreen
from kivy.uix.screenmanager import ScreenManager

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
from network_handler import NetworkHandler

class RootScreenManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootScreenManager()
    

if __name__ == "__main__":
    MainApp().run()

