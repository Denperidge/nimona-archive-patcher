# Nimona Archive Patcher
Patches for the Nimona webcomic archive, including (but not limited to):

- Removing the artists deadname ([code](patches/replace_chapter_1_page_1.py), [jpg](assets/chapter-1/page-1.jpg))
- Normalising file extensions ([code](patches/jpegs_to_jpg.py)) 
- Splitting the chapter titles from the rest of the page ([code](patches/seperate_chapter_title.py))
- Splitting the pages into panels ([code](patches/split_to_panels.py), [library](https://github.com/Denperidge/comicstrip))
- Adding alt-text (TODO)

## Usage
```bash
git clone https://github.com/Denperidge/nimona-archive-patcher.git
cd nimona-archive-patcher

python3.10 -m pip install git+https://github.com/Denperidge/comicstrip
cp -r ../path/to/extracted/ .

python3.10 index.py
```

### (Optional) Upload to a file server
tar -czvf patched.tar.gz ./patched/
scp patched.tar.gz DOMAIN_OR_IP:/srv/nimona-archive/
