from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation

from .functions import Voice

import pyaudio
import numpy as np
import threading

class Recognizer_btn(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.voice = Voice()
        self.send_message = False
        self.first_request = True
        self.request_message = ""
        
        self.always_release = False
        self.size_hint = (None, None)
        self.size = (200, 75)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        self.num_bars = 7
        self.max_height = 35
        self.base_height = 20
        self.bar_heights = [self.base_height] * self.num_bars
        self.pressed = False
        self.volume = 0
        self.CHUNK = 1021
        self.RATE = 44100
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.thread = None
        Clock.schedule_interval(self.update_canvas, 1/30)
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def audio_thread(self):
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)
        while self.pressed:
            try:
                data = np.frombuffer(self.stream.read(self.CHUNK, exception_on_overflow=False), dtype=np.int16)
                self.volume = np.abs(data).mean() / 5000
            except Exception:
                pass
        self.stream.stop_stream()
        self.stream.close()
        self.stream = None
        self.volume = 0
              
    def on_press(self):
        self.pressed = True
        self.thread = threading.Thread(target=self.audio_thread, daemon=True)
        self.thread.start()
        
        print("recognition started")
        self.voice.start_recording()
            
    def on_release_thread(self):
        self.send_message = True
        anim = Animation(pos_hint={"center_x": 0.5, "center_y": 0.16}, duration=1)
        anim.start(self)
        
        self.pressed = False
        if self.thread:
            self.thread.join()
        self.bar_heights = [self.base_height] * self.num_bars
        self.volume = 0
        
        print("recognition ended")
        self.request_message = self.voice.end_recording()
        print(f"text: {self.request_message}")
            
    def on_release(self):
        threading.Thread(target=self.on_release_thread).start()
        
    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0, 0, 0, 0.5)
            Rectangle(pos=self.pos, size=self.size)
            Color(1, 1, 1, 0.6)
            bar_width = 15
            gap = 10
            y_center = self.y + self.height / 2

            total_width = self.num_bars * bar_width + (self.num_bars - 1) * gap
            start_x = self.x + (self.width - total_width) / 2 

            for i in range(self.num_bars):
                if self.pressed:
                    delta = np.random.rand() * self.volume * (self.max_height - self.base_height)
                    h_top = self.base_height + delta
                    h_bottom = self.base_height + delta
                else:
                    h_top = self.base_height
                    h_bottom = self.base_height

                x = start_x + i * (bar_width + gap)

                Rectangle(pos=(x, y_center), size=(bar_width, h_top))
                Rectangle(pos=(x, y_center - h_bottom), size=(bar_width, h_bottom))

