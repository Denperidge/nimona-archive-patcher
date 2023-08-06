from os import makedirs
from glob import glob
from os.path import exists, dirname
from json import load, dump

def merge_assets_json(pages):
    for page in pages:
        patched_json_path = "patched/" + page.replace(".jpg", ".json")
        assets_json_path = "assets/" + page.replace(".jpg", ".json")

        with open(patched_json_path, "r") as file:
            patched_json = load(file)

        with open(assets_json_path, "r") as file:
            assets_json = load(file)

        
        with open(patched_json_path, "w", encoding="UTF-8") as file:
            data = dict()
            data.update(patched_json)
            data.update(assets_json)
            dump(data, file)
      
