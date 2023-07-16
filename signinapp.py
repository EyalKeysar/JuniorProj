from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import ObjectProperty, Clock
from network_handler import NetworkHandler


class MainWindow(Screen):
    pass

class LogInWindow(Screen):
    pass

class SignUpWindow(Screen):
    pass

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        print("WindowManager init")
        super().__init__(**kwargs)


class SignInApp(App):
    def build(self):
        kv = Builder.load_file("signin.kv")
        return kv
        

