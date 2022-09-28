import subprocess
import time
import pyautogui
import pandas as pd
from datetime import datetime

def sign_in(meeting_id):
    '''subprocess.call(["/C:/Users/giris/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Zoom"]);'''
    subprocess.call(["C:/Users/giris/AppData/Roaming/Zoom/bin/Zoom.exe"])

    time.sleep(5)
    join_btn = pyautogui.locateCenterOnScreen('jb.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    time.sleep(5)
    meeting_id_btn = pyautogui.locateCenterOnScreen('meeting_id_img.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meeting_id)




    time.sleep(5)
    meeting_join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(meeting_join_btn)
    pyautogui.click()

    time.sleep(5)
    got_it_btn = pyautogui.locateCenterOnScreen('got_it.png')
    pyautogui.moveTo(got_it_btn)
    pyautogui.click()

    '''time.sleep(5)
    meeting_leave_btn = pyautogui.locateCenterOnScreen('leave_btn.png')
    pyautogui.moveTo(meeting_leave_btn)
    pyautogui.click()

    time.sleep(5)
    confirm_leave_btn = pyautogui.locateCenterOnScreen('leave_confirm_btn.png')
    pyautogui.moveTo(confirm_leave_btn)
    pyautogui.click()'''

df = pd.read_csv('datasheet.csv')
while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):
        sign_in('91259269552')
        #sign_in('96105910326')
