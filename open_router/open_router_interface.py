import json
import requests
class OpenRouter():
    def __init__(self, api_key: str, model_name: str, completions_url: str = "https://openrouter.ai/api/v1/chat/completions"): 
        self.api_key = api_key
        self.completions_url = completions_url
        self.model = model_name
        self.headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
        }
    
    # Sends a message
    def send_message(self, message: dict) -> json.JSONEncoder:
        payload = {
            "model": self.model,
            "messages": [message] # Must be a list
        }

        response = requests.post(
            url = self.completions_url,
            headers=self.headers,
            json=payload
        ) 
        return response.json()