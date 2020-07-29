import shutil

from config import name, temp_folder, win_out, x11_out
from os import path, listdir


package_dir = "./packages"
x11_out_dir = path.join(package_dir, x11_out)
win_out_dir = path.join(package_dir, win_out)


def init_build() -> None:
    if path.exists(package_dir):
        shutil.rmtree(package_dir)


def cleanup() -> None:
    """
        🧹 Clean the unnecessary directorys & generate archive files.
    """
    # Rename directory
    shutil.move(path.join(temp_folder, name, "x11"), x11_out_dir)
    shutil.move(path.join(temp_folder, name, "win"), win_out_dir)

    # Packaging
    #  - .tar archive for X11
    #  - .zip archive for Windows
    shutil.make_archive(x11_out_dir, "tar", x11_out_dir)
    shutil.make_archive(win_out_dir, "zip", win_out_dir)

    # Clenaup
    shutil.rmtree(temp_folder)
    for f in listdir(package_dir):
        f_path = path.join(package_dir, f)
        if path.isdir(f_path):
            shutil.rmtree(f_path)