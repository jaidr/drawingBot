import pyautogui as pg
import keyboard

# go from left to right while mouse down (on cooldown)
# go down 6 pixels
# hard coded example to speed up 'blanking'/ canvas creation process for my computer
for y in range(34):
    if keyboard.is_pressed("b"):
        break
    pg.moveTo(860,452+y*6,duration=0.5)
    pg.mouseDown()
    pg.moveRel(202,0,duration=0.8)
    pg.mouseUp()
