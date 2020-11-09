from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position X:  725 Y:  500 RGB: ( 87,  89, 117)
#Tile 2 Position X:  902 Y:  500 RGB: ( 89,  91, 117)
#Tile 3 Position X: 1023 Y:  500 RGB: (  0,   0,   0)
#Tile 4 Position X: 1161 Y:  500 RGB: ( 90,  91, 118)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
    
    if pyautogui.pixel(725,500)[0] == 0:
       click(725,500)
    if pyautogui.pixel(902,500)[0] == 0:
       click(902,500)
    if pyautogui.pixel(1023,500)[0] == 0:
       click(1023,500)
    if pyautogui.pixel(1161,500)[0] == 0:
       click(1161,500)    
