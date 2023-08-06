from os import makedirs
from os.path import exists, dirname
from json import load, dump


def generate_transcript_structure(pages):
    for page in pages:
        base_path = "assets/" + page.replace(".jpg", "")

        makedirs(dirname(base_path), exist_ok=True)

        path = base_path + ".json"

        if not exists(path):
            with open(path, "w", encoding="UTF-8") as file:
                dump(
                    {
                        "alt": "",
                        "image-description": ""
                    }, file)
        else:
            with open(path, "r", encoding="UTF-8") as file:
                data = load(file)
                if data["alt"] == "":
                    print(f"[{path}] Missing alt text")
                if data[("image-description")]:
                    print(f"[{path}] Missing image description")

            

            
        


