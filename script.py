import os.path
import requests
from clint.textui import progress
import json

import logging
import threading
from threading import Thread
import time

# Android termux path:
SAVE_PATH = "/storage/524C-AE60/Android/data/com.termux/Comics/"
# SAVE_PATH = "/Users/eau/Documents/"
MAX_THREADS = 5


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
    print(name)
    complete_name = os.path.join(SAVE_PATH, name)
    r = requests.get(link, allow_redirects=True, stream=True)

    # code from https://stackoverflow.com/questions/15644964/python-progress-bar-and-downloads
    # adds progress bar to stdout for download
    with open(complete_name, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

def main():
    # print("Loading JSON")

    settings = {
    "save_path" : "/storage/524C-AE60/Android/data/com.termux/Comics/",
    "max_threads" : "5"
    }

    new_search = {
    "search_query" : "ascender",
    "last_update" : "10/12/2019",
    }


    links = [
    "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L1dlZWtseSUyMFJlbGVhc2UvMjAxOS4wNi4wNS9VcDEvQmlydGhyaWdodCUyMDAzNiUyMCUyODIwMTklMjklMjAlMjhkaWdpdGFsJTI5JTIwJTI4U29uJTIwb2YlMjBVbHRyb24tRW1waXJlJTI5LmNicg==",
    "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L1dlZWtseSUyMFJlbGVhc2UvMjAxOS4wNi4wNS9VcDIvQ3JpbWluYWwlMjAwMDUlMjAlMjgyMDAxOSUyOSUyMCUyOERpZ2l0YWwtRW1waXJlJTI5LmNicg==",
    "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L1dlZWtseSUyMFJlbGVhc2UvMjAxOS4wNi4wNS9VcDEvRWNsaXBzZSUyMDAxNiUyMCUyODIwMTklMjklMjAlMjhEaWdpdGFsJTI5JTIwJTI4Wm9uZS1FbXBpcmUlMjkuY2Jy",
    "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L1dlZWtseSUyMFJlbGVhc2UvMjAxOS4wNi4wNS9VcDIvUGFwZXIlMjBHaXJscyUyMDAyOSUyMCUyODIwMDE5JTI5JTIwJTI4RGlnaXRhbC1FbXBpcmUlMjkuY2Jy"
    ]

    names = [
    "Birthright 36.cbr",
    "Criminal 5.cbr",
    "Eclipse 16.cbr",
    "Paper Girls #29.cbr"
    ]

    threads = []
    for i in range(len(links)):
        print(i)
        threads.append(Thread(target=download_comic, args=(links[i], names[i])))

    for i in range(len(threads)):
        threads[i].start()



# Ascender download link
# download_link = "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L090aGVycy9JbWFnZSUyMENvbWljcy9DaGV3L0NoZXclMjB2MDElMjAtJTIwVGFzdGVyJTI3cyUyMENob2ljZSUyMCUyODIwMDklMjklMjBHZXRDb21pY3MuSU5GTy5jYnI="
# download_comic(download_link, "Chew Vol 1.cbr")

main()
