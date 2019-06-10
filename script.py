import os.path
import requests
from clint.textui import progress
import json

import logging
import threading
import time

# Android termux path:
SAVE_PATH = "/storage/524C-AE60/Android/data/com.termux/Comics/"
# SAVE_PATH = "/Users/eau/Documents/"

SEARCH_QUERIES = []

def shell():
    print("Shell started.")
    while True:
        input_line = input(": ").lower()
        input_array = input_line.split()

        if input_array[0] == "exit":
            break

        elif input_array[0] == "print":
            print("print")

        elif input_array[0] == "run":
            print("run")

    print("Shell closed.")

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

def main():
    print("Loading JSON")

    new_search = {
    "search_query" : "ascender",
    "last_update" : "10/12/2019",

    }



# Ascender download link
download_link = "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L090aGVycy9JbWFnZSUyMENvbWljcy9DaGV3L0NoZXclMjB2MDElMjAtJTIwVGFzdGVyJTI3cyUyMENob2ljZSUyMCUyODIwMDklMjklMjBHZXRDb21pY3MuSU5GTy5jYnI="
download_comic(download_link, "Chew Vol 1.cbr")

main()
