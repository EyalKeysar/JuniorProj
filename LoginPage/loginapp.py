import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config

class LoginGrid(Widget):
    pass

class LoginApp(App):
    def build_config(self, config):
        Config.set('graphics', 'resizable', False)
        return super().build_config(config)

    def build(self):
        return LoginGrid()
    
    
    
LoginApp().run()