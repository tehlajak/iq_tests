import base64
import json
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def save_json(fname: str, content):
    try:
        with open(fname, "w") as f:
            json.dump(content, f, indent=4)
        print(f"Contents saved to {fname}!")
    except:
        print(f"Could not save to {fname}")
