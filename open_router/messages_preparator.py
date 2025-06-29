from utils import *
import os

class Preparator():
    """ This class prepares the messages in json format """
    def __init__(self, 
                 prompt: str,
                 answer_sheet_path: str,
                 save_dir: str,
                 encode_images: bool = True
                 ):
        """
        Initializes the class with the provided parameters.

        Args:
            prompt (str): Prompt for the LLM.
            answer_sheet_path (str): Path to the answer sheet (.csv file), used to extract image paths.
            save_dir (str): Path to the directory where the created JSON file containing messages will be saved.
            encode_images (bool, optional): Whether to encode images as base64 or use URLs. Defaults to True.
        """
        self.prompt = prompt
        self.answer_sheet_path = answer_sheet_path
        self.save_dir = save_dir
        self.encode_images = encode_images
        self.message_format_placeholder =         {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": ""
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": ""
                    }
                }
            ]
        }
    
    def __str__(self):
        print(f"""
              Preparator settings:\n
                - prompt: '\n{self.prompt}'\n
                - answer_sheet_path: {self.answer_sheet_path}
                - save_dir: {self.save_dir}
                - encode_images: {self.encode_images}
              """)
    
    def fill_message_format(self, prompt: str, data_url: str) -> dict:
        message_format = self.message_format_placeholder
        message_format["content"][0]["text"] = prompt
        message_format["content"][1]["image_url"]["url"] = data_url
        return message_format 
    
    def prepare_json(self):
        answers_df = load_csv(self.answer_sheet_path)
        
        messages = []
        # message_index = 0
        # Iterate through the answers dataframe and extract image paths 
        for img_path in answers_df["image_path"]:
            base64_img = encode_image_to_base64(img_path)
            data_url = f"data:image/jpeg;base64,{base64_img}"

            message = self.fill_message_format(self.prompt, data_url=data_url)

            # messages.append(
            #     {
            #         message_index: message
            #     }
            # )
            messages.append(message)
            # message_index += 1
        
        # Save as json
        ensure_dir(self.save_dir)
        save_path = os.path.join(self.save_dir, "messages.json")
        save_json(save_path, messages)
