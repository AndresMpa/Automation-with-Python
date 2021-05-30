import doctest as dt
from sys import argv as argv
from os import scandir as scan
from pathlib import Path as ObjectPath

DIRS_EXTENTION = {
    '~': ['order.py'],
    'Música': ['.mp3', '.ogg'],
    'Imágenes': ['.jpeg', '.jpg', '.png'],
    'Documentos': ['.docx', '.xlsx', '.ppxt','.cvs', '.pdf', '.txt'],
}

def pickDir(value):
    """
    This function analize from a given dictionary
    where should a file be redirectioned

    >>> pickDir('.pdf')
    'Documentos'

    >>> pickDir(None)
    'Escritorio'

    >>> pickDir('.mp4')
    'Escritorio'
    """

    for category, extention in DIRS_EXTENTION.items():
        for file in extention:
            if file == value:
                return category
    return 'Escritorio'
dt.testmod()

def organizeDirs():
    for item in scan():
        if item.is_dir():
            continue
        filePath = ObjectPath(item)
        fileType = filePath.suffix.lower()
        directory = pickDir(fileType)
        directoryPath = ObjectPath(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirs()
