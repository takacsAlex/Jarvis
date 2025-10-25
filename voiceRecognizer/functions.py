import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer
from dotenv import load_dotenv
import os

class Voice_recognition:
    def __init__(self, model_path, sample_rate=16000):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, sample_rate)
        self.sample_rate = sample_rate
        self.q = queue.Queue()
        
    def callback(self, indata, frames, time, status):
        if status:
            print("Hangfelvétel: ", status)
        self.q.put(bytes(indata))
        
    def recognize_once(self, duration=5):
        
        print(f"Hallgatás {duration} másodpercig")
        with sd.RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype='int16',
            channels=1,
            callback=self.callback
        ):
            sd.sleep(int(duration * 1000))  # várunk ennyi ideig
            data = b"".join(list(self.q.queue))  # összegyűjtjük a mintákat
            self.q.queue.clear()
            
        if self.recognizer.AcceptWaveform(data):
            result = json.loads(self.recognizer.Result())
            return result.get("text", "")
        else:
            partial = json.loads(self.recognizer.PartialResult())
            return partial.get("partial", "")