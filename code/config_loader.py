import json

def get_config(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf-8") as file:
        dict = json.load(file)
    return dict