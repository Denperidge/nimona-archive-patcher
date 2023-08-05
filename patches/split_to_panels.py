from comicstrip import Page  # Install from https://github.com/denperidge/comicstrip

def split_into_panels(pages):
    for page in pages:   
        output_name = "patched/" + page.replace(".jpg", "")

        Page("patched/" + page).save(output_name + "-")
