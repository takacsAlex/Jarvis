import speech_recognition
import threading
import time

class Voice():
    def __init__(self):
        self.recording = False
        self.audio_chunks = []
        self.thread = None
        self.recognizer = speech_recognition.Recognizer()

    def record_loop(self):
        with speech_recognition.Microphone() as mic:
            self.recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            while self.recording:
                try:
                    chunk = self.recognizer.record(mic, duration=1)  
                    self.audio_chunks.append(chunk)
                except Exception:
                    time.sleep(0.1)
            
    def start_recording(self):
        self.audio_chunks = []
        self.recording = True
        self.thread = threading.Thread(target=self.record_loop, daemon=True)
        self.thread.start()
        
    def end_recording(self):
        self.recording = False
        
        if self.thread:
            self.thread.join()
            
        if not self.audio_chunks:
            return ""
        
        try:
            raw = b"".join([c.get_raw_data() for c in self.audio_chunks])
            sample_rate = self.audio_chunks[0].sample_rate
            sample_width = self.audio_chunks[0].sample_width

            combined = speech_recognition.AudioData(raw, sample_rate, sample_width)
            
            text = self.recognizer.recognize_google(combined, language="hu-HU")
            return text.lower()
        except Exception as e:
            return f"there is a problem with the voice recognition"
        
        