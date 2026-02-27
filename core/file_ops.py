# file_ops.py
import os
from tkinter import filedialog

TEMP_DIR = "temp_files"

def ensure_temp_dir():
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

def save_image(image, default_name="image.png"):
    path = filedialog.asksaveasfilename(
        defaultextension=".png",
        initialfile=default_name,
        filetypes=[("PNG Image", "*.png")]
    )
    if path:
        image.save(path)
        return path
    return None

def save_temp_image(image, filename):
    ensure_temp_dir()
    path = os.path.join(TEMP_DIR, filename)
    image.save(path)
    return path

def cleanup_temp():
    if not os.path.exists(TEMP_DIR):
        return
    for f in os.listdir(TEMP_DIR):
        try:
            os.remove(os.path.join(TEMP_DIR, f))
        except:
            pass
