from os import makedirs
from glob import glob
from os.path import exists, dirname
from yaml import safe_dump, safe_load, representer

def str_presenter(dumper, data):
    """configures yaml for dumping multiline strings
    Ref: https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data"""
    if data.count('\n') > 0:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

representer.SafeRepresenter.add_representer(str, str_presenter)

default_transcript_text = "Write text\nhere"

def handle_transcripts(pages):
    print(pages)
    for page in pages:
        path = "assets/" + page.replace(".jpg", ".yml")

        panels = glob("*", root_dir="patched/" + page.replace(".jpg", "/"))
        panels = [panel.replace(".jpg", "") for panel in panels]

        if not exists(path):
            data = dict({
                "image-description": default_transcript_text,
                "alt-texts": {}
            })

            for panel in panels:
                panel = panel
                data["alt-texts"][panel] = default_transcript_text
                
            with open(path, "w", encoding="UTF-8") as file:
                safe_dump(data, file, sort_keys=False)
                
                
                
        else:
            with open(path, "r", encoding="UTF-8") as file:
                data = safe_load(file)
                if data["image-description"] == "":
                    print(f"[{path}] Missing image description text")
                
                for panel in panels:
                    panel = panel
                    if panel not in data["alt-texts"]:
                        print(f"[{path}] ERROR: no alt-text key for {panel}")
                    elif data["alt-texts"][panel] == default_transcript_text:
                        print(f"[{path}] Missing alt-text entry for {panel}")
