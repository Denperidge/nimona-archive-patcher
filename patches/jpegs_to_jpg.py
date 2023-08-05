from pathlib import Path

def jpegs_to_jpg():
    jpegs = Path("patched/").glob("**/*.jpeg")
    for jpeg in jpegs:
        jpeg.rename(jpeg.with_suffix(".jpg"))
