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
    def __init__(self, network_handler, **kwargs):
        super().__init__(**kwargs)
        self.network_handler = network_handler
        Clock.schedule_interval(self.connection_bar_update, 1.0 / 60.0)

    def connection_bar_update(self, dt):
        self.connection_status_bar.color = (0, 1, 0, 1) if self.network_handler.connection_status else (1, 0, 0, 1)

class SignInApp(App):

    def __init__(self, logger, **kwargs):
        super().__init__(**kwargs)
        self.logger = logger
        self.connection_status = False
        self.network_handler = NetworkHandler(self.logger)

    def build(self):
        self.logger.log(" * Built game ----------------------------------------------------------------")
        window_manager = WindowManager(network_handler=self.network_handler)
        self.network_handler.CreateSocket()
        Clock.schedule_interval(self.network_update, 1.0 / 60.0)
        return window_manager
    
    def run(self):
        self.logger.log(" * Running game")
        return super().run()
    
    def network_update(self, dt):
        self.network_handler.CheckConnection()
        self.update_connection_status_bar()

    def update_connection_status_bar(self):
        self.connection_status = self.network_handler.connection_status
        

