from os import makedirs
from glob import glob
from os.path import exists, dirname
from yaml import safe_load
from json import load, dump


def load_data(path, load_func):
    if exists(path):
        with open(path, "r") as file:
            data = load_func(file)
    else:
        data = ""
    return data

def merge_yml_to_json(assets_yml_path, patched_json_path):
    patched_data = load_data(patched_json_path, load)

    assets_data = load_data(assets_yml_path, safe_load)

    with open(patched_json_path, "w", encoding="UTF-8") as file:
        data = dict()
        data.update(patched_data)
        data.update(assets_data)
        dump(data, file)


def merge_pages_data(pages):
    for page in pages:
        patched_json_path = "patched/" + page.replace(".jpg", ".json")
        assets_yml_path = "assets/" + page.replace(".jpg", ".yml")

        merge_yml_to_json(assets_yml_path, patched_json_path)
      
def add_character_data(chapters):
    for chapter in chapters:
        print(chapter)
        patched_json_path = f"patched/{chapter}/chapter.json" 
        assets_yml_path = f"assets/{chapter}/characters.yml"

        merge_yml_to_json(assets_yml_path, patched_json_path)