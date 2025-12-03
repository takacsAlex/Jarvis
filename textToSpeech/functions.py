from gtts import gTTS
from io import BytesIO
import pygame
import time

def wait():
    while pygame.mixer.get_busy():
        time.sleep(1)
        
def speak(text, lang="hu"):
    mp3 = BytesIO()
    tts = gTTS(text, lang=lang)
    tts.write_to_fp(mp3)
    mp3.seek(0)
    sound = pygame.mixer.Sound(mp3)
    sound.play()
    wait()
    
