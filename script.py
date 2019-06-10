import os.path
import requests
from clint.textui import progress

# Android termux path:
save_path = "/storage/524C-AE60/Android/data/com.termux/Comics/"
# SAVE_PATH = "/Users/eau/Documents/"

def download_comic(link, name):
    complete_name = os.path.join(SAVE_PATH, name)
    r = requests.get(download_link, allow_redirects=True, stream=True)

    # code from https://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads
    with open(complete_name, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

# Ascender download link
download_link = "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L090aGVycy9JbWFnZSUyMENvbWljcy9DaGV3L0NoZXclMjB2MDElMjAtJTIwVGFzdGVyJTI3cyUyMENob2ljZSUyMCUyODIwMDklMjklMjBHZXRDb21pY3MuSU5GTy5jYnI="
download_comic(download_link, "Chew Vol 1.cbr")
