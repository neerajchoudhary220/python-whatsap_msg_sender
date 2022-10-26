import pyautogui
import time
from pynput.keyboard import Key, Controller
Keyboard = Controller()

def sendmsg(limit,msg,path):
    x0,y0 = pyautogui.locateCenterOnScreen(path, grayscale= True, confidence=0.9)
    # pyautogui.click(200, 100)
    time.sleep(2)
    pyautogui.click(x0, y0)
    limit = int(limit)
    for x in range(limit):
        Keyboard.type(msg)
        pyautogui.press('enter')

