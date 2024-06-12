import keyboard
import mouse
import time 

def change():
    global work
    work = not work

work = False
keyboard.add_hotkey(',', change)

while True:
    if work:
        mouse.click(button='left')
        time.sleep(0.00001)