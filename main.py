from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from front.dashboard.voice_recognizer_widget import Recognizer
from kivy.resources import resource_find

import os

class Dashboard(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        background_video_path = "front/images_videos/background.mp4"
        self.background = Video(source=background_video_path, state="play", eos="loop")
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
