import os.path
import requests

# Android termux path:
save_path = "/storage/524C-AE60/Android/data/com.termux/Comics/"
# save_path = "/Users/eau/Documents/"

# Ascender download link
download_link = "https://getcomics.info/go.php-urls/aHR0cDovL3Rlbi5jb21pY2ZpbGVzLnJ1L1dlZWtseSUyMFJlbGVhc2UvMjAxOS4wNS4yOS9VcDEvQXNjZW5kZXIlMjAwMDIlMjAlMjgyMDE5JTI5JTIwJTI4RGlnaXRhbCUyOSUyMCUyOFpvbmUtRW1waXJlJTI5LmNicg=="
complete_name = os.path.join(save_path, "ascender.cbr")

r = requests.get(download_link, allow_redirects=True)
open(complete_name, 'wb').write(r.content)

# name_of_file = input("What is the name of the file: ")
#
# completeName = os.path.join(save_path, name_of_file+".txt")
#
# file1 = open(completeName, "w")
#
# toFile = input("Write what you want into the field: ")
#
# file1.write(toFile)
#
# file1.close()
