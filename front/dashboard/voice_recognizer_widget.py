from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from voiceRecognizer.functions import Voice

class VoiceRecognizer(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Recognizer())

class Recognizer(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Recognizer_btn())
    
class Recognizer_btn(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.voice = Voice()
        self.always_release = False  #enable cancellation
        self.text = "Start"
        self.color = (1, 0, 0, 1)
        self.size_hint = (None, None)
        self.size = (200, 100)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
           
    def on_press(self):
        print("recognition started")
        self.voice.start_recording()
            
    def on_release(self):
        print("recognition ended")
        text = self.voice.end_recording()
        print(f"text: {text}")