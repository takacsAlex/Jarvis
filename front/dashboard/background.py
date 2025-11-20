from kivy.uix.video import Video
from kivy.uix.floatlayout import FloatLayout


class Background(Video):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "front/images_videos/background.mp4"
        self.state = "play"
        self.opacity = 0.5