import os
import shutil


def delete_directory_contents(path: str):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)


def copy_tree_helper(src: str, dest: str):
    for filename in os.listdir(src):
        src_path = os.path.join(src, filename)
        dest_path = os.path.join(dest, filename)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            os.mkdir(dest_path)
            copy_tree_helper(src_path, dest_path)


def copy_tree(src: str, dest: str):
    delete_directory_contents(dest)
    copy_tree_helper(src, dest)
