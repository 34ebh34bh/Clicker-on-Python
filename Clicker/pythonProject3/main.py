from os import times
import keyboard
import mouse
import time

isClicking = False


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Clicker activated')
    else:
        isClicking = True
        print('Clicker off')

keyboard.add_hotkey('w', set_clicker)

while True:
    if isClicking:
        mouse.double_click(button='left')
        time.sleep(0.01)