import requests
import json

def post_ai(url, text):
    headers = {
        "Content-Type": "application/json"
    }
    prompt = {
        "message": text
    }
    
    response = requests.post(url=url, headers=headers, json=prompt)
    result = response.json()
    
    if result.get("status") == "success":
        return result["response"]
    else:
        return "There is a problem with the artificial intelligence"