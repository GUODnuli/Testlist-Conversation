import json

def config_dict(config_path: str) -> dict:
    with open(config_path, "r") as file:
        dict = json.load(file)
    return dict