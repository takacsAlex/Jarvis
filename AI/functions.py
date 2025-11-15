import requests

def post_ai(url, text):
    headers = {
        "Content-Type": "application/json"
    }
    
    basic_instructons = "The user is hungarian, so you have to speak hungarian too. You're name is Dzsárvisz, if the user asks you and you are a helping robot!"
    
    prompt = {
        "message": basic_instructons + text
    }
    
    response = requests.post(url=url, headers=headers, json=prompt)
    result = response.json()
    
    if result.get("status") == "success":
        return result["response"]
    else:
        return "There is a problem with the artificial intelligence"