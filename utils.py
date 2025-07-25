import os, sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller .exe"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
