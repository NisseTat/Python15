import os
import logging
import stat

from collections import namedtuple
from argparse import ArgumentParser

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

logging.basicConfig(filename='directory_contents.log', level=logging.INFO, format='%(message)s', filemode='w')
def dir_info(dir_path):

    if not os.path.isdir(dir_path):
        raise ValueError(f"{dir_path} - не директория!!!")

    parent_directory = os.path.basename(os.path.abspath(dir_path))

    for entry in os.listdir(dir_path):
        entry_path = os.path.join(dir_path, entry)

        if os.path.isdir(entry_path):
            flag_mode = os.stat(entry_path).st_mode
            flag = stat.filemode(flag_mode)
            info = FileInfo(name=entry, extension=flag, is_directory=True, parent_directory=parent_directory)
        else:
            name, extension = os.path.splitext(entry)
            info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)

        logging.info(f'{info.name} | {info.extension if info.extension else "???"} | {"Директория" if info.is_directory else "Файл"} | {info.parent_directory}')

parser = ArgumentParser()
parser.add_argument('dir', type=str, help="Путь")
args = parser.parse_args()
dir_path = args.dir

try:
    dir_info(dir_path)
except ValueError as e:
    print(e)