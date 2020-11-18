#! /usr/bin/python

import pyautogui
import time

print(pyautogui.position())
pyautogui.moveTo(606, 1000)
pyautogui.click()

with open("BeeMovie.txt", "r") as file:

   for i in file:
       i = i.rstrip()
       if len(i) > 0:
          i = i.split()
          for j in i:
              pyautogui.write(str(j))
              pyautogui.press("enter")
