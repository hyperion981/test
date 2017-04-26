#coding=utf-8

import os
import time

count_time=0

for num_time in range(100):
    os.system('adb shell input keyevent 223')
    time.sleep(2)
    os.system('adb shell input keyevent 224')
    time.sleep(1)
    os.system('adb shell input swipe 300 1000 300 500')
    time.sleep(3)
    count_time += 1

print count_time