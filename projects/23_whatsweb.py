import pyautogui
import time
time.sleep(1)
count = 0
while count<=10:
     pyautogui.typewrite("hello world this is wroten by python program",str(count))
     pyautogui.press("enter")
     count=count+1