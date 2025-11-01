#for iphone 13 configs
from kivy.config import Config
Config.set('graphics', 'width', '390')
Config.set('graphics', 'height', '844')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from voiceRecognizer.functions import Voice_recognition
from aI.functions import post_ai
from textToSpeech.functions import text_to_speech

from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    model = os.getenv("VOICE_MODEL")
    recognizer = Voice_recognition(model_path=model)
    
    print("Kezdjük a hangfelismerést...")
    text = recognizer.recognize_once(duration=5)
    print(text)
    
    ai_response = post_ai(url=os.getenv("AI_ENDPOINT"), text=text)
    print(ai_response)
    text_to_speech(ai_response)
    
GUI = Builder.load_file("jarvis.kv")
    
class Jarvis(App):
    def build(self):
        return GUI
