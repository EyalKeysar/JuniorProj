import kivy
from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.widget import Widget


kivy.require('2.2.1') 

class MainGrid(Widget):
    pass

class MainApp(App):
    def build(self):
        return MainGrid()

MainApp().run()