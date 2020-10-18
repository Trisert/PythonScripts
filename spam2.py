#! /usr/bin/python

import pyautogui
import os

pyautogui.moveTo(1529, 891)
pyautogui.press("i")

file = open("Numeri.txt", "a")

for i in range(0,201):
   file.write(str(i))
   file.write("\n")
file.close()

files = open("Numeri.txt", "r")

for i in files:
    i = i.rstrip()
    if len(i) > 0:
        i = i.split()
        for j in i:
            pyautogui.write(str(j))
            pyautogui.press("enter")

os.remove("Numeri.txt")

