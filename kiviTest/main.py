import kivy
from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('graphics', 'resizable', False)

kivy.require('2.2.1') 

class MainGrid(Widget):
    name = ObjectProperty(None)

    def btn(self):
        print(f'Hello {self.name.text}')
        self.name.text = ""

class MainApp(App):
    def build(self):
        return MainGrid()

MainApp().run()