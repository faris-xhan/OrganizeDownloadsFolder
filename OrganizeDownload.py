#! python
# OrganizeDownload - Organize your download folder
import os
from time import time
from math import floor


# Returns the current timestamp
def timestamp():
    return floor(time())


def moveFile(path, folderName, file):
    if file == __file__:
        pass

    dst = os.path.join(path, folderName)
    if not(os.path.exists(dst)):
        os.mkdir(dst)
    try:
        os.rename(file, dst)
    except FileExistsError:
        fileName = os.path.basename(file)
        name, ext = os.path.splitext(fileName)
        name += ' - ' + str(timestamp())
        fileName = name + ext
        dst = os.path.join(dst, fileName)
        os.rename(file, dst)

    print(f'{file} --> {dst}')


Home = os.getenv('USERPROFILE') or os.getenv('HOME')
Downloads = os.path.join(Home, 'Downloads')


if not os.path.exists(Downloads):
    print('Sorry! for some reason script could not find your Download folder')
    exit(127)

# Change Directory to Downloads
os.chdir(Downloads)

document = ('doc', 'xls', 'pdf', 'docx', 'txt')
pictures = ('jpeg', 'jpg', 'png', 'gif')
videos = ('mkv', 'avi', 'mp4', 'ts')
compressed = ('zip', 'rar', '7z')
programs = ('exe', 'bat', 'msi')
music = ('mp3', 'wav')

for file in os.listdir():
    if os.path.isfile(file):
        file = os.path.realpath(file)
        path, fileName = os.path.split(file)
        if file.endswith(pictures):
            moveFile(path, 'Pictures', file)

        elif file.endswith(compressed):
            moveFile(path, 'Compressed', file)

        elif file.endswith(videos):
            moveFile(path, 'Videos', file)

        elif file.endswith(music):
            moveFile(path, 'Music', file)

        elif file.endswith(document):
            moveFile(path, 'Documents', file)

        elif file.endswith(programs):
            moveFile(path, 'Programs', file)

        else:
            moveFile(path, 'Others', file)
