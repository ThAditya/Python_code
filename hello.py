#for unlimited msgs on wtsp
import pyautogui
import time
time.sleep(7)
count=0
while count<=50:
    pyautogui.typewrite("hello")
    pyautogui.press("enter")
    count=count+1