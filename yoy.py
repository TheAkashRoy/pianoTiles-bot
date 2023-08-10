from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# X: 335 Y: 800 RGB: (0,0,0,0)
# X: 444 Y: 800 RGB: (0,0,0,0)
# X: 565 Y: 800 RGB: (0,0,0,0)
# X: 682 Y: 800 RGB: (0,0,0,0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.07)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    # if pyautogui.pixel(335,800)[0]==0:
    click(366,944)