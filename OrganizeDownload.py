#! python
# OrganizeDownload - Organize your download folder

import os
from time import time
from math import floor
from pathlib import Path

SCRIPT_NAME = Path(__file__).name

# Directories
HOME_DIR = os.getenv('USERPROFILE') or os.getenv('HOME')
DOWNLOADS_DIR = Path(os.path.join(HOME_DIR, 'Downloads'))

COMPRESSED_DIR = Path(os.path.join(DOWNLOADS_DIR, 'Compressed'))
DOCUMENTS_DIR = Path(os.path.join(DOWNLOADS_DIR, 'Documents'))
PROGRAMS_DIR = Path(os.path.join(DOWNLOADS_DIR, 'Programs'))
PICTURES_DIR = Path(os.path.join(DOWNLOADS_DIR, 'Pictures'))
OTHERS_DIR = Path(os.path.join(DOWNLOADS_DIR, 'Others'))
VIDEOS_DIR = Path(os.path.join(DOWNLOADS_DIR, 'Videos'))
MUSIC_DIR = Path(os.path.join(DOWNLOADS_DIR, 'Music'))

# Files Extensions
document = ('doc', 'xls', 'pdf', 'docx', 'txt')
pictures = ('jpeg', 'jpg', 'png', 'gif')
videos = ('mkv', 'avi', 'mp4', 'ts')
compressed = ('zip', 'rar', '7z')
programs = ('exe', 'bat', 'msi')
music = ('mp3', 'wav')


def timestamp():
    # Returns the current timestamp
    return floor(time())


def moveFile(file, destination_dir):
    filename = Path(file).name
    destination = Path(destination_dir, filename)
    if filename == SCRIPT_NAME:
        return

    if not(os.path.exists(destination_dir)):
        os.mkdir(destination_dir)

    try:
        os.rename(file, destination)

    except FileExistsError:
        new_filename = file.stem + ' - ' + str(timestamp())
        destination = os.path.join(destination_dir, new_filename)

        os.rename(file, destination_dir)

    print(f'{file.name} --> {destination_dir.name}')


if not DOWNLOADS_DIR.exists():
    print('Sorry! for some reason script could not find your Download folder')
    exit(127)

# Change Directory to Downloads
os.chdir(DOWNLOADS_DIR)


for file in os.listdir():
    file = Path(file)

    if file.exists() and file.is_file():
        filename = file.name
        if filename.endswith(pictures):
            moveFile(file, PICTURES_DIR)

        elif filename.endswith(compressed):
            moveFile(file, COMPRESSED_DIR)

        elif filename.endswith(videos):
            moveFile(file, VIDEOS_DIR)

        elif filename.endswith(music):
            moveFile(file, MUSIC_DIR)

        elif filename.endswith(document):
            moveFile(file, DOCUMENTS_DIR)

        elif filename.endswith(programs):
            moveFile(file, PROGRAMS_DIR)

        else:
            moveFile(file,  OTHERS_DIR)
