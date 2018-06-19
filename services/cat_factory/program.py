import os
import platform
import subprocess
from cat_service import *

from services.cat_factory import cat_service


def main():
    # print the header
    print_header()

    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)

    download_cats(folder)

    display_cat(folder)


def print_header():
    print("----------------------------")
    print("----------LOL CAT FACOTRY----------")
    print("----------------------------")
    print()



def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pics'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Requesting server ...  ')
    cat_count = 8
    for i in range(1, cat_count):
        name = 'lolcat_{}'.format(i)
        print('Downloading ... cat ' + name)
        cat_service.get_cat(folder, name)

    print('Download Done')


def display_cat(folder):
    # open folder
    if platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    elif platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['start', folder])
    else:
        print('We dont support your OS ' + platform.system())


if __name__ == '__main__':
    main()