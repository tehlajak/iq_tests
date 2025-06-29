from api_keys import *
import requests
import json
from utils import *
from typing import List, Any
from dataset_preparator import *
from prompts import *
from constants import *
import os


def send_image(completions_url: str, img_url: str, api_key: str) -> Any:
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
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Is the sun in the picture?"
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
    response = requests.post(completions_url, headers=headers, json=payload)
    print(response.json())
    json_response = response.json()
    save_json("test.json", json_response)


def send_encoded_image(completions_url: str, image_path: str, api_key: str):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    base64_img = encode_image_to_base64(image_path=image_path)
    data_url = f"data:image/jpeg;base64,{base64_img}"
    
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
                        "url": data_url
                    }
                }
            ]
        }
    ]

    payload = {
        "model": "google/gemini-2.0-flash-001",
        "messages": messages
    }
    response = requests.post(completions_url, headers=headers, json=payload)
    print(response.json())
    json_response = response.json()
    save_json("test2.json", json_response)

def main():
    completions_url = "https://openrouter.ai/api/v1/chat/completions"
    
    
    dataset_type = "4_comp"
    for dataset in datasets:
        messages_save_dir = os.path.join("../messages", dataset_type, dataset)
        
        answer_sheet_path = f"../data/Datasets/answers/Testing/{dataset_type}/{dataset_type}_{dataset}_answers.csv"
        dataset_prep = Preparator(prompt=cot_prompt,
                                answer_sheet_path=answer_sheet_path,
                                save_dir=messages_save_dir,
                                )

        dataset_prep.prepare_json()
    

if __name__ == "__main__":
    main()