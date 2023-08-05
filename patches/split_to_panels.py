from comicstrip import Page
from os import remove

def patch_split_to_panels(pages):
    for page in pages:   
        output_name = "patched/" + page.replace(".jpg", "")

        Page("patched/" + page).save(output_name + "-")
