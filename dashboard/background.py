from kivy.uix.video import Video

class Background(Video):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "dashboard/images_videos/background.mp4"
        self.state = "play"
        self.opacity = 0.5
        self.options = {"eos": "loop"}