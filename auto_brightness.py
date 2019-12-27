import os
import cv2
import numpy as np
import pyautogui
from time import sleep

def change_brightness(calibrated):
    active = "POWERCFG /S 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
    ac_change = "POWERCFG /SETACVALUEINDEX 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 7516b95f-f776-4464-8c53-06167f40cc99 aded5e82-b909-4619-9949-f5d71dac0bcb " + str(calibrated)
    dc_change = "POWERCFG /SETDCVALUEINDEX 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 7516b95f-f776-4464-8c53-06167f40cc99 aded5e82-b909-4619-9949-f5d71dac0bcb " + str(calibrated)
    os.system(dc_change)
    os.system(ac_change)
    os.system(active)

while(True):
    ss = pyautogui.screenshot()
    ss = np.array(ss)
    ss = cv2.resize(ss,(96,54))
    ss = cv2.cvtColor(ss,cv2.COLOR_BGR2RGB)
    ss = cv2.cvtColor(ss,cv2.COLOR_BGR2GRAY)
    calibrated = (100-(((np.mean(ss)*100)/255)))*0.6
    change_brightness(calibrated=int(calibrated))
    sleep(0.1)
