from os import makedirs
from glob import glob
from os.path import exists, dirname
from yaml import safe_load
from json import load, dump

def merge_assets_data(pages):
    for page in pages:
        patched_json_path = "patched/" + page.replace(".jpg", ".json")
        assets_yml_path = "assets/" + page.replace(".jpg", ".yml")

        with open(patched_json_path, "r") as file:
            patched_data = load(file)

        with open(assets_yml_path, "r") as file:
            assets_data = safe_load(file)

        
        with open(patched_json_path, "w", encoding="UTF-8") as file:
            data = dict()
            data.update(patched_data)
            data.update(assets_data)
            dump(data, file)
      
