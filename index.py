from glob import glob
from comicstrip import Page
from shutil import rmtree, copytree

from patches.seperate_chapter_title import patch_seperate_chapter_title
from patches.split_to_panels import patch_split_to_panels

pages = glob("**/page-1.jpg", recursive=True, root_dir="patched/")


rmtree("patched/", ignore_errors=True)
copytree("extracted/", "patched/")

patch_seperate_chapter_title(pages)
patch_split_to_panels(pages)
