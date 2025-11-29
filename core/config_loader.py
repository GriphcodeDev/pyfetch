import json 
import os

def loader():
    base = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base, "..", "config.json")

    if not os.path.exists(config_path):
        return {}


    with open(config_path, "r") as f:
        return json.load(f)
