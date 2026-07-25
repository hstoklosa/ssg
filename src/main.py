import sys

from copystatic import copy_tree
from generate_content import generate_pages_recursive

STATIC_DIR_PATH = "./static"
PUBLIC_DIR_PATH = "./docs"
CONTENT_DIR_PATH = "./content"
TEMPLATE_PATH = "./template.html"


def main() -> None:
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_tree(STATIC_DIR_PATH, PUBLIC_DIR_PATH)
    generate_pages_recursive(CONTENT_DIR_PATH, TEMPLATE_PATH, PUBLIC_DIR_PATH, basepath)


main()
