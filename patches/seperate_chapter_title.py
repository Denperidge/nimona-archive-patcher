from glob import glob
from os import makedirs
from os.path import dirname
from PIL import Image


def patch_seperate_chapter_title(pages, chapter_height=120):
    for page in pages:
        if page.endswith("page-1.jpg"):
            img = Image.open("patched/" + page)
            img.crop((0, 0, img.width, chapter_height)).save("patched/" + page.replace("page-1", "chapter"))
            
            img.crop((0, chapter_height, img.width, img.height)).save("patched/" + page)

