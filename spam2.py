#! /usr/bin/python

import pyautogui
import os

pyautogui.moveTo(1529, 891)
pyautogui.click()
pyautogui.press("i")

with open("Numeri.txt", "a") as file:

   for i in range(0,1000000):
      file.write(str(i))
      file.write("\n")
   file.close()

with open("Numeri.txt", "r") as files:

   for i in files:
       i = i.rstrip()
       if len(i) > 0:
          i = i.split()
          for j in i:
              pyautogui.write(str(j))
              pyautogui.press("enter")

os.remove("Numeri.txt")

