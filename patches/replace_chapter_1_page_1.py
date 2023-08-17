from os import system, makedirs
from os.path import abspath, dirname

def replace_chapter_1_page_1(archived_page="extracted/chapter-1/page-1.jpg", patched_page="assets/chapter-1/page-1.jpg", output_page="patched/chapter-1/page-1.jpg"):
    archived_page = abspath(archived_page).replace("\\", "/")
    patched_page = abspath(patched_page).replace("\\", "/")
    output_page = abspath(output_page).replace("\\", "/")

    makedirs("patched/chapter-1/", exist_ok=True)
    system(f'ffmpeg -y -i {archived_page} -i {patched_page} -map 1 -c copy -map_metadata 0 {output_page}')
