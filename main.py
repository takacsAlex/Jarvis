#for iphone 13 configs
from kivy.config import Config
Config.set('graphics', 'width', '390')
Config.set('graphics', 'height', '844')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from front.dashboard.voice_recognizer_widget import VoiceRecognizer

GUI = Builder.load_file("front/jarvis.kv")
    
class Jarvis(App):
    
    def build(self):
        return GUI
    
    def screen_change(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name
