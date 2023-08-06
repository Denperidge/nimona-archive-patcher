from os import makedirs
from comicstrip import Page  # Install from https://github.com/denperidge/comicstrip

def split_into_panels(pages):
    for page in pages:
        page_dir = "patched/" + page.replace(".jpg", "") + "/"
        makedirs(page_dir, exist_ok=True)

        Page("patched/" + page).save(page_dir + "panel-", counter=1)
