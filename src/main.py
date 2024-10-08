import os
import shutil
from helper import *

def main():
    print("Deleting Public dir")
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    print("Copying static dir to public dir")
    copy_static_to_public("./static", "./public")

    generate_pages_recursive("./content", "./template.html", "./public")

main()