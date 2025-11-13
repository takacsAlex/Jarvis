#for iphone 13 configs
from kivy.config import Config
Config.set('graphics', 'width', '390')
Config.set('graphics', 'height', '844')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from voiceRecognizer.functions import voice_recognition
from aI.functions import post_ai
from textToSpeech.functions import speak

from dotenv import load_dotenv
import os

import pygame


class VoiceRecognizer(Screen):
    pass

class WaitingLobby(Screen):
    pass

class Output(Screen):
    pass
     
GUI = Builder.load_file("front/jarvis.kv")
    
class Jarvis(App):
    def build(self):
        return GUI
    
    def screen_change(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name
        
    def sending_voice_to_ai(self):
        try:
            print("voice recording started!")
            text = voice_recognition()
            print(text)
        except Exception as e:
            print(f"voice recognition error : {e}")
        
        try:
            load_dotenv()
            response = post_ai(url=os.getenv("AI_ENDPOINT"), text=text)
            print(response)
            
            pygame.init()
            pygame.mixer.init()
            speak(response)
        except Exception as e:
            print(f"waiting lobby error : {e}")