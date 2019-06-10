import os
import os.path
import requests
from clint.textui import progress
import json

import logging
import threading
from threading import Thread
import time
import random

# Android termux path:
SAVE_PATH = "/storage/524C-AE60/Android/data/com.termux/Comics/"
# SAVE_PATH = "/Users/eau/Documents/"
MAX_THREADS = 5

SETTINGS = {
    "save_path" : "/",
    "max_threads" : 1
}


SEARCH_QUERIES = []

def shell():
    print("Shell started.")
    while True:
        input_line = input(": ")
        input_array = input_line.split()

        if input_array[0] == "exit":
            break

        elif input_array[0] == "print":
            print("print")

        elif input_array[0] == "run":
            print("run")

        elif input_array[0] == "set":
            if input_array[1] == "save_path":
                new_path(input_array)
            elif input_array[1] == "max_threads":
                new_max_threads(input_array)

    print("Shell closed.")


def new_path(input_array):
    new_path = ""
    if len(input_array) != 3:
        new_path = input("New path: ")
    else:
        new_path = input_array[2]

    # test path exists
    passed = False
    test_text = "testing file path"
    key = str(random.randint(0, 1000000000))
    test_file_name = "testfile_" + key + ".txt"
    try:
        complete_test_file = os.path.join(new_path, test_file_name)
        with open(complete_test_file, 'w+') as test_file:
            test_file.write(test_text)

        os.remove(complete_test_file)
        passed = True

    except:
        print("Path test failed.")
        passed = False

    # set new path, save to JSON
    if passed:
        SETTINGS["save_path"] = new_path
        writeSettings()
        print("Wrote new path to settings.json")

def new_max_threads(input_array):
    new_max_threads = 1
    if len(input_array) != 3:
        new_max_threads = int(input("New max_threads: "))
    else:
        new_max_threads = input_array[2]

    # set new path, save to JSON
    SETTINGS["max_threads"] = new_max_threads
    writeSettings()
    print("Wrote new max_threads to settings.json")

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

def loadSettings():
    try:
        with open("settings.json", 'r') as settings_file:
            SETTINGS = json.load(settings_file)

    except FileNotFoundError:
        writeSettings()

def writeSettings():
    with open("settings.json", 'w+') as settings_file:
        json.dump(SETTINGS, settings_file)

def main():
    # print("Loading JSON")

    new_search = {
    "search_query" : "ascender",
    "last_update" : "10/12/2019",
    }

    loadSettings()

    shell()






    # links = [
    # "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L1dlZWtseSUyMFJlbGVhc2UvMjAxOS4wNi4wNS9VcDEvQmlydGhyaWdodCUyMDAzNiUyMCUyODIwMTklMjklMjAlMjhkaWdpdGFsJTI5JTIwJTI4U29uJTIwb2YlMjBVbHRyb24tRW1waXJlJTI5LmNicg==",
    # "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L1dlZWtseSUyMFJlbGVhc2UvMjAxOS4wNi4wNS9VcDIvQ3JpbWluYWwlMjAwMDUlMjAlMjgyMDAxOSUyOSUyMCUyOERpZ2l0YWwtRW1waXJlJTI5LmNicg==",
    # "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L1dlZWtseSUyMFJlbGVhc2UvMjAxOS4wNi4wNS9VcDEvRWNsaXBzZSUyMDAxNiUyMCUyODIwMTklMjklMjAlMjhEaWdpdGFsJTI5JTIwJTI4Wm9uZS1FbXBpcmUlMjkuY2Jy",
    # "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L1dlZWtseSUyMFJlbGVhc2UvMjAxOS4wNi4wNS9VcDIvUGFwZXIlMjBHaXJscyUyMDAyOSUyMCUyODIwMDE5JTI5JTIwJTI4RGlnaXRhbC1FbXBpcmUlMjkuY2Jy"
    # ]
    #
    # names = [
    # "Birthright 36.cbr",
    # "Criminal 5.cbr",
    # "Eclipse 16.cbr",
    # "Paper Girls #29.cbr"
    # ]
    #
    # threads = []
    # for i in range(len(links)):
    #     print(i)
    #     threads.append(Thread(target=download_comic, args=(links[i], names[i])))
    #
    # for i in range(len(threads)):
    #     threads[i].start()


main()
