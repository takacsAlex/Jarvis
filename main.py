from kivy.app import App
from kivy.uix.screenmanager import Screen
from dashboard.main import Recognizer
from dashboard.background import Background

class Dashboard(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)    
        self.background = Background()
        self.add_widget(self.background)
        self.recognizer = Recognizer()
        self.add_widget(self.recognizer)

class Jarvis(App):
    def build(self):
        return Dashboard()
