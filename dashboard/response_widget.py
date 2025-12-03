from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class Response_widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.response_change, 0.1)
        
        self.response_message = "..."
        
        with self.canvas:
            Color(0, 0, 0, 0.6)
            Rectangle(pos=(250, 175), size=(250, 375))
            
        self.response = Label(
            size=(250, 375),
            text=self.response_message,
            text_size=(222, None),
            pos_hint={"center_x": 0.47, "center_y": 0.83},
            color=(1, 1, 1, 1),
            bold=True
        )
        self.add_widget(self.response)
    
    def response_change(self, dt):
        if self.response_message != "...":
            self.remove_widget(self.response)
            self.add_widget(self.response)
            