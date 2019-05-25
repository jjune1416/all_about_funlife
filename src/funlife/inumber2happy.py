# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:29:26 2019

@author: ghost
"""

# pip install pygetwindow=0.0.1
# pip install pyautogui

import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()

def oneLoop(m_inumber) :
    print ("start {}".format(m_inumber))
    #쿠폰 입력창
    pyautogui.moveTo(650, 297)
    pyautogui.doubleClick()
    time.sleep(0.5)
    #입력
    pyautogui.typewrite(m_inumber)
    time.sleep(0.5)
    
    #입력완료
    pyautogui.click(650, 954)
    time.sleep(0.8)
    
    #충전확인
    pyautogui.click(592, 582)
    time.sleep(0.8)
    pyautogui.click(592, 582)
    time.sleep(0.8)
    
    #
    pyautogui.click(674, 950, clicks=2, interval=0.7)
    time.sleep(1.4)
    print ("done {}".format(m_inumber))
    
    #오류방지
    pyautogui.click(592, 582)
    time.sleep(0.5)

def parse_text(text_file) :
    coupon_list = []
    with open(text_file, "r", encoding='euc-kr') as f:
        for line in f.readlines():
            if line.startswith("* 쿠폰번호 : ") :
                single_coupon = line.replace("* 쿠폰번호 : ", '').replace("-", '').replace('\n', '')
                coupon_list.append(single_coupon)
    return list(dict.fromkeys(coupon_list))


inumber_file = "./raw_inumber_text.txt"
inumber_list = parse_text(inumber_file)
print (inumber_list)
print ("count {}".format(len(inumber_list)))

for inumber in inumber_list : 
    oneLoop(inumber)
