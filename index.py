from glob import glob
from shutil import rmtree, copytree

from patches.replace_chapter_1_page_1 import replace_chapter_1_page_1
from patches.jpegs_to_jpg import jpegs_to_jpg
from patches.seperate_chapter_title import seperate_chapter_title
from patches.split_to_panels import split_into_panels
from patches.generate_transcript_structure import handle_alt_files, handle_transcripts
from patches.merge_assets_json import merge_assets_json

def patch(patch, selector="*"):
    pages = glob(f"**/{selector}.jpg", recursive=True, root_dir="patched/")
    patch(pages)

print("Select mode:")
print("0: Check transcription progress")
print("1: Created patched/")

mode = int(input("Mode: "))

if mode == 1:
    rmtree("patched/", ignore_errors=True)
    copytree("extracted/", "patched/")

    # Run patches that can run without params
    jpegs_to_jpg()
    replace_chapter_1_page_1()

    patch(seperate_chapter_title, "page-1")
    patch(split_into_panels, "page-*")
    patch(merge_assets_json, "page-*")

#patch(handle_alt_files, "panel-*")
patch(handle_transcripts, "page-*")