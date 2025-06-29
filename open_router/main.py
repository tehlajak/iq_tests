import argparse
from api_keys import *
import requests
import json
from utils import *
from typing import List, Any
from messages_preparator import *
from prompts import *
from constants import *
import os
from open_router_interface import *

def main(dataset_type: str, dataset: str):
    OR = OpenRouter(api_key=IQ_KEY_1, 
                    model_name=model,
                    structured_output=True)

    messages_save_dir = os.path.join("../messages", dataset_type, dataset, prompt)
    responses_save_dir = os.path.join("../responses", dataset_type, dataset, prompt, model)
    ensure_dir(responses_save_dir)

    messages_path = os.path.join(messages_save_dir, "messages.json")
    messages_data = load_json(messages_path)

    for run in range(0, NUM_RUNS):
        json_responses = []
        for message in messages_data:
            json_response = OR.send_message(message)
            json_responses.append(json_response)
        responses_save_path = os.path.join(responses_save_dir, f"run_{run}.json")
        save_json(responses_save_path, json_responses)

    print(f"Finished processing dataset '{dataset}' under type '{dataset_type}'.")

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run OpenRouter experiments on a specific dataset")
    parser.add_argument("--dataset_type", required=True, help="Type of the dataset (3_comp or 4_comp)")
    parser.add_argument("--dataset", required=True, help="Dataset name to process (e.g. oa_os_oc)")

    args = parser.parse_args()
    main(dataset_type=args.dataset_type, dataset=args.dataset)