from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from .voiceRecognizer.voice_recognizer_widget import Recognizer_btn
from .response_widget import Response_widget
from aI.functions import AI

class Recognizer(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.first_request, 0.3)
        Clock.schedule_interval(self.request, 0.5)
        
        self.ai = AI()
        self.button = Recognizer_btn()
        self.label = Response_widget()
        self.add_widget(self.button)
        
    def first_request(self, dt):
        if self.button.pos_hint == {"center_x": 0.5, "center_y": 0.16} and self.button.first_request:
            self.add_widget(self.label)
            self.button.first_request = False
        
    def request(self, dt):
        if self.button.send_message and self.button.pos_hint == {"center_x": 0.5, "center_y": 0.16} and not self.button.first_request:
            self.ai.request = self.button.request_message
            self.ai.post_ai()
            self.button.send_message = False
            
        if self.ai.response != "":
            response = self.ai.response
            self.label.response.text = response
            self.ai.response = ""

