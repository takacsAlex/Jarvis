#for iphone 13 configs
# from kivy.config import Config
# Config.set('graphics', 'width', '390')
# Config.set('graphics', 'height', '844')
# Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from front.dashboard.voice_recognizer_widget import Recognizer
# from front.dashboard.background import Background

import os
from kivy.resources import resource_find

class Dashboard(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        print(os.path.exists("front\\images_videos\\background.mp4"))
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        video_path = os.path.join(BASE_DIR, "front", "images_videos", "background.mp4")
        self.background = Video(source=video_path, state="play", eos="loop")
        self.background.opacity = 0.5
        self.add_widget(self.background)
        self.add_widget(Recognizer())

GUI = Builder.load_file("front/jarvis.kv")
    
class Jarvis(App):
    
    def build(self):
        return GUI
    
    def screen_change(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name
