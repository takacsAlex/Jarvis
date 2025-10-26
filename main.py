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
    
    
if __name__ == "__main__":
    main()