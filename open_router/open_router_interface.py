import json
import requests
class OpenRouter():
    def __init__(self,
                api_key: str,
                model_name: str,
                structured_output: bool=True,
                completions_url: str = "https://openrouter.ai/api/v1/chat/completions"): 
        self.api_key = api_key
        self.completions_url = completions_url
        self.model = model_name
        self.structured_output = structured_output
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

        if self.structured_output:
            payload = {
                "model": self.model,
                "messages": [message], # Must be a list
                "response_format": {
                    "type": "json_schema",
                    "json_schema": {
                        "name": "iq_test_reasoning",
                        "strict": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Description of the reasoning process"
                                },
                                "prediction": {
                                    "type": "string",
                                    "description": "A single letter response containing the selected prediction."
                                }
                            },
                            "required": ["reasoning", "prediction"],
                            "additionalProperties": False
                        }
                    }
                }
            }
        response = requests.post(
            url = self.completions_url,
            headers=self.headers,
            json=payload
        ) 
        return response.json()