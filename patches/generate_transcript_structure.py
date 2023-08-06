from os import makedirs
from glob import glob
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


def handle_transcripts(pages):
    print(pages)
    for page in pages:
        path = "assets/" + page.replace(".jpg", ".json")

        panels = glob("*", root_dir="patched/" + page.replace(".jpg", "/"))
        panels = [panel.replace(".jpg", "") for panel in panels]

        if not exists(path):
            data = dict({
                "image-description": "",
                "alt-texts": {}
            })

            for panel in panels:
                panel = panel
                data["alt-texts"][panel] = ""
                
            with open(path, "w", encoding="UTF-8") as file:
                dump(data, file)
                
                
                
        else:
            with open(path, "r", encoding="UTF-8") as file:
                data = load(file)
                if data["image-description"] == "":
                    print(f"[{path}] Missing image description text")
                
                for panel in panels:
                    panel = panel
                    if panel not in data["alt-texts"]:
                        print(f"[{path}] ERROR: no alt-text key for {panel}")
                    elif data["alt-texts"][panel] == "":
                        print(f"[{path}] Missing alt-text entry for {panel}")
            
