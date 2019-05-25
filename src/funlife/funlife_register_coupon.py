# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:53:27 2019

@author: ghost
"""

import time
import sys

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Chrome('../bin/chromedriver')
driver.implicitly_wait(3)

with open("./idpw.conf") as f:
    my_id = f.readline()
    my_pw = f.readline()

#login
def login(id, pw):
    try :
        driver.get('http://my.funpass.co.kr/users/login')
        id_cont = driver.find_element_by_id('user_id')
        id_cont.clear()
        id_cont.send_keys(id)
        pw_cont = driver.find_element_by_id('password')
        pw_cont.clear()
        pw_cont.send_keys(pw)
        driver.find_element_by_class_name('login_btn').click()
    except KeyboardInterrupt :
        sys.exit(1)
    except :
        return False
    try :
        driver.get('http://my.funpass.co.kr/mall/shop/3')
        driver.find_element_by_partial_link_text('로그인').click()
    except :
        return True
    return False

while(not login(my_id, my_pw)) : pass

def wait_and_accept_alert(f_driver) :
    try :
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException :
        return False
    return True

def register_one_coupon(f_driver, coupon) :
    coupon_id_element = driver.find_element_by_id('coupon_id')
    coupon_id_element.clear()
    coupon_id_element.send_keys(coupon)
    f_driver.find_element_by_xpath("//div/div/div/div/span/button").click()
    while not wait_and_accept_alert(f_driver):
        pass
    while not wait_and_accept_alert(f_driver):
        pass
        
def parse_text(text_file) :
    coupon_list = []
    with open(text_file) as f:
        for line in f.readlines():
            if line.startswith("＊쿠폰번호 : ") :
                single_coupon = line.replace("＊쿠폰번호 : ", '').replace('-', '').replace('\n', '')
                coupon_list.append(single_coupon)
    return coupon_list


driver.get('http://my.funpass.co.kr/mypage/coupon')

text_file_path = "./raw_coupon_text.txt"
coupon_list = parse_text(text_file_path)
print ('coupon list')
print (coupon_list)
print ()

count = 0
for coupon in coupon_list : 
    register_one_coupon(driver, coupon)
    print('registered [{}]'.format(coupon))
    count += 1

print('total [{}] coupon registered'.format(str(count)))