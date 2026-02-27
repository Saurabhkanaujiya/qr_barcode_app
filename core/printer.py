# printer.py
import os
import sys
import subprocess
from .file_ops import save_temp_image

def print_image(image, filename="print_image.png"):
    path = save_temp_image(image, filename)

    if sys.platform.startswith("win"):
        os.startfile(path, "print")
    elif sys.platform.startswith("darwin"):
        subprocess.run(["lp", path])
    else:
        subprocess.run(["lp", path])
