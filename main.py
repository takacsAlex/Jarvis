from voiceRecognizer.functions import Voice_recognition
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    model = os.getenv("VOICE_MODEL")
    recognizer = Voice_recognition(model_path=model)
    
    print("🎧 Kezdjük a hangfelismerést...")
    text = recognizer.recognize_once(duration=5)
    print("🗣️ Felismert szöveg:", text)
    
if __name__ == "__main__":
    main()