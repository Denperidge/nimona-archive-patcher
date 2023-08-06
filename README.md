# Nimona Archive Patcher
[Visit the website here](http://nimona.neonpastel.net/) - [Check out the website repo](https://github.com/Denperidge/Nimona-Archive)

Patches for the Nimona webcomic archive, including (but not limited to):

- Removing the artists deadname ([code](patches/replace_chapter_1_page_1.py), [jpg](assets/chapter-1/page-1.jpg))
- Normalising file extensions ([code](patches/jpegs_to_jpg.py)) 
- Splitting the chapter titles from the rest of the page ([code](patches/seperate_chapter_title.py))
- Splitting the pages into panels ([code](patches/split_to_panels.py), [library](https://github.com/Denperidge/comicstrip))
- Adding alt-text & image descriptions ([code](patches/generate_transcript_structure.py), [text](assets/))

This script will output a `patched/` folder, which will then be used to generate the website. See [the website repository here](https://github.com/Denperidge/Nimona-Archive)


## How-to
### Running
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


## Discussions
### Extracted folder
As you may have noticed, you need the `extracted/` folder to run this script. The reasons why this folder isn't publicly available is the same as with the patched folder. You can read as to why [in the website repository's README](https://github.com/Denperidge/Nimona-Archive#patched-folder).


## License
- Nimona comic: I do not own Nimona, nor am I affiliated with its owners.
- Patches: all the code in this repository is licensed under the [MIT license](LICENSE)
- Assets: all the transcriptions/alt texts are available under (TODO: figure out which license is most appropiate)
