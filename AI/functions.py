from dotenv import load_dotenv
import requests
import threading
import os


class AI:
    def __init__(self):
        self.basic_instructions = "The user is hungarian, so you have to speak hungarian too. You're name is Jarvis, if the user asks you and you are a helping robot! Don't use any emojis!"
        self.request = ""
        self.response = ""
        
        
    def post_ai_thread(self):
        headers = {
            "Content-Type": "application/json"
        }
        prompt = {
            "message": self.basic_instructions + self.request
        }
        
        load_dotenv()
        url = os.getenv("AI_ENDPOINT")
        
        print("sending request to the ai")
        response = requests.post(url=url, headers=headers, json=prompt)
        result = response.json()
        
        if result.get("status") == "success":
            self.response = result["response"]
        else:
            self.response = "There is a problem with the artificial intelligence" 
        print(self.response)       
        
    def post_ai(self):
        threading.Thread(target=self.post_ai_thread, daemon=True).start()