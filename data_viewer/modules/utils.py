import os

def getFullPath(filename):
    #__file__ is inbuilt python variable which return the full path of the current file utils.py
    crtdir = os.path.dirname(__file__)

    print(f"crtdir:{crtdir}")

    pardir = os.path.abspath(os.path.join(crtdir, os.pardir))

    print(f"pardir:{pardir}")
    return f"{pardir}/{filename}"