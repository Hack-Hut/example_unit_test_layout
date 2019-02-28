import os

def walk(path):
    return os.walk(path)

def exists(path):
    if os.path.exists(path):
        return True
    return False

def extension(path):
    filename, file_extension = os.path.splitext(path)
    return file_extension