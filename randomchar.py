#! /usr/bin/python

import pyautogui
import random
import string

ascii = string.ascii_letters + string.digits + '{$+,’^>?!|{!£>¥}!]$#+!}!¥'

while True:
    pyautogui.write(random.choice(ascii))
