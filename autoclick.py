import pyautogui
import time
import pygetwindow as gw

# windows = gw.getActiveWindowWithTitle('Google Chrome')
# # 4147 2025 2590 9519
# # 01/27 269
# # we pay flight ticket
# for screen in windows:
#     print(f"{screen}")
pyautogui.click(300,300)
time.sleep(2)
while True:
    pyautogui.press('0')
    pyautogui.press('s')
    pyautogui.press('y')
    # pyautogui.locateOnScreen(image="right arrow.png", region=(1353, 196, 1437, 291))
    pyautogui.click(1383, 233)
    time.sleep(10)
    print("wait 10 seconds")