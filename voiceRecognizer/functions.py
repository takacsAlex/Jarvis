import speech_recognition

def voice_recognition():
    recognizer = speech_recognition.Recognizer()

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic, timeout=None, phrase_time_limit=None)
                
            text = recognizer.recognize_google(audio, language="hu-HU")
            text = str(text).lower()
            
            return text
                
    except Exception as e:
            return e