#!/usr/bin/env python3

import pyautogui
import time
import keyboard

pyautogui.PAUSE = 0

#X:  350 Y:  662 RGB: (255, 255, 255)
#X:  467 Y:  646 RGB: (255, 255, 255)
#X:  572 Y:  673 RGB: ( 17,  17,  17)
#X:  672 Y:  647 RGB: (255, 255, 255)

#X:  362 Y:  558 RGB: (255, 255, 255)
#X:  456 Y:  560 RGB: (255, 255, 255)
#X:  574 Y:  563 RGB: ( 17,  17,  17)
#X:  675 Y:  563 RGB: (255, 255, 255)


while True:

    if pyautogui.pixel(362, 558)[0] == 17:
        pyautogui.click(362, 558, button='left')
    if pyautogui.pixel(465, 560)[0] == 17:
        pyautogui.click(465, 560, button='left')
    if pyautogui.pixel(574, 563)[0] == 17:
        pyautogui.click(574, 563, button='left')
    if pyautogui.pixel(675, 563)[0] == 17:
        pyautogui.click(675, 563, button='left')
