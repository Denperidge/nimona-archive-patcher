from os import makedirs
from os.path import exists, dirname
from json import load, dump


def handle_alt_files(panels):
    for panel in panels:
        base_path = "assets/" + panel.replace(".jpg", "")

        makedirs(dirname(base_path), exist_ok=True)

        path = base_path + ".alt.txt"

        if not exists(path):
            with open(path, "w", encoding="UTF-8"):
                pass
        else:
            with open(path, "r", encoding="UTF-8") as file:
                data = file.read()
                if data == "":
                    print(f"[{path}] Missing alt text")


def handle_image_description_files(pages):
    for page in pages:
        path = "assets/" + page.replace(".jpg", ".image-description.txt")

        if not exists(path):
            with open(path, "w", encoding="UTF-8"):
                pass
        else:
            with open(path, "r", encoding="UTF-8") as file:
                data = file.read()
                if data == "":
                    print(f"[{path}] Missing image description text")
