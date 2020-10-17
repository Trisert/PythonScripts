#! /usr/bin/python

import shutil
import os
import glob

fullpath = os.path.join
python_directory = "/home/nicola/Python"
start_directory = "/home/nicola"

def main():
    for dirname, dirnames, filenames in os.walk(start_directory):
        for filename in filenames:
            source = fullpath(dirname, filename)
            if filename.endswith("py"):
                shutil.move(source, fullpath(python_directory, filename))

if __name__ == "__main__":
    main()
