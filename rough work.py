import pyautogui
import time


from datetime import datetime



# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
# print(now.minute)
# print(now.hour)
# print(pyautogui.position())

# im3 = pyautogui.screenshot(region=(0,0, 300, 400))
#
# im3.save(r"C:\Users\butteke\OneDrive - Ecolab\Desktop\snapshot.png")

#snapshot locatio Point(x=94, y=53) to Point(x=1122, y=933)

while datetime.now().hour < 14:
    # now = datetime.now()
    pyautogui.press('volumedown')
    time.sleep(1)
    # pyautogui.press('volumeup')
    # print(now.minute)
    time.sleep(150)