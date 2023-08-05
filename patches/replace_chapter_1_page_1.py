from os import system

def replace_chapter_1_page_1(page="patched/chapter-1/page-1.jpg", img="assets/chapter-1/page-1.jpg"):


    system(f'ffmpeg -y -i "{page}" -i {img} -map 1 -c copy -map_metadata 0 "patched/chapter-1/page-1.jpg"')
