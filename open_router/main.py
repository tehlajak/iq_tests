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

def main():
    OR = OpenRouter(api_key=IQ_KEY_1, 
                    model_name=model,
                    structured_output=True)

    dataset_type = "3_comp"
    for dataset in datasets:
        messages_save_dir = os.path.join("../messages", dataset_type, dataset, prompt)
        responses_save_dir = os.path.join("../responses", dataset_type, dataset, prompt, model)
        ensure_dir(responses_save_dir)
        # answer_sheet_path = f"../data/Datasets/answers/Testing/{dataset_type}/{dataset_type}_{dataset}_answers.csv"
        # dataset_prep = Preparator(prompt=prompts[prompt],
        #                         answer_sheet_path=answer_sheet_path,
        #                         save_dir=messages_save_dir,
        #                         )
        # dataset_prep.prepare_json()
        messages_path = os.path.join(messages_save_dir, "messages.json")
        messages_data = load_json(messages_path)

        for run in range(0, NUM_RUNS):
            json_responses = []
            # print(f"run: {run}, dataset: {dataset}")
            # print(len(messages_data))
            for message in messages_data:
                json_response = OR.send_message(message)
                json_responses.append(json_response)
            responses_save_path = os.path.join(responses_save_dir, f"run_{run}.json")
            save_json(responses_save_path, json_responses)
        print()
    
    
if __name__ == "__main__":
    main()