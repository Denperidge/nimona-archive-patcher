from os import makedirs
from os.path import exists, dirname


def generate_transcript_structure(pages):
    for page in pages:
        base_path = "assets/" + page.replace(".jpg", "")

        makedirs(dirname(base_path), exist_ok=True)

        alt_path = base_path + ".alt.txt"
        id_path = base_path + ".id.txt"

        for path in [alt_path, id_path]:
            if not exists(path):
                with open(path, "w"):
                    pass
        


