from api_keys import *
import requests
import json
from typing import List, Any


def send_image(img_url: str, api_key: str) -> Any:
    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
    }
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"{img_url}"
                    }
                }
            ]
        }
    ]
    payload = {
        "model": "google/gemini-2.0-flash-001",
        "messages": messages
    }
    response = requests.post(img_url, headers=headers, json=payload)
    print(response.json())

def main():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
    send_image(url, IQ_KEY_1)

if __name__ == "__main__":
    main()