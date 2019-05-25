# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:00:14 2019

@author: ghost
"""

from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import sys

def login(id,pw):
    driver.get('https://ssl.g9.co.kr/Member/CustomerService/AllLogin')
    
    id_cont = driver.find_element_by_id("MemberLoginM_MemberID")
    id_cont.clear()
    id_cont.send_keys(id)
    
    pw_cont = driver.find_element_by_id("MemberLoginM_MemberPassword")
    pw_cont.clear()
    pw_cont.send_keys(pw)
    
    driver.find_element_by_id('btnDoLoginJson').click()

def wait_and_switch_window() :
    try :
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException :
        return False
    return True

def purchase(purchase_5 = False, purchase_double = False) :
    url_funlife_10 = 'http://www.g9.co.kr/Display/VIP/Index/1564093326'
    url_funlife_5 = 'http://www.g9.co.kr/Display/VIP/Index/1564094522'

    if purchase_5 :
        print("purchase 5")
        driver.get(url_funlife_5)
    else :
        print("purchase 10")
        driver.get(url_funlife_10)
    
    if purchase_double :
        driver.find_element_by_class_name("plus").click()
    
    #driver.get("http://www.g9.co.kr/Display/VIP/Index/1261909554")
    time.sleep(2)
    driver.find_element_by_class_name("btn_buy").click()

    buyer_name_cont = driver.find_element_by_id("buyerName")
    buyer_name_cont.clear()
    buyer_name_cont.clear()
    time.sleep(0.3)
    buyer_name_cont.send_keys('백인준')
    
    phone_middle_cont = driver.find_element_by_name("receiveHPNo2")
    phone_middle_cont.clear()
    phone_middle_cont.clear()
    time.sleep(0.3)
    phone_middle_cont.send_keys('6409')
    
    phone_last_cont = driver.find_element_by_name("receiveHPNo3")
    phone_last_cont.clear()
    phone_last_cont.clear()
    time.sleep(0.3)
    phone_last_cont.send_keys('9696')
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    driver.find_element_by_id('methodPayment03').send_keys(' ')
    driver.find_element_by_xpath("//div/div/ul/li/span/label/span[@class='sp_or']").click()
    driver.find_element_by_class_name('ico_hd').click()
    driver.find_element_by_xpath("//div[@id='payment_method']/div/div/div/div/div/div/div/div/span/label/span[@class='sp_or']").click()
    
    driver.execute_script("window.scrollTo(0, 0);")
    
    #driver.find_element_by_class_name("btn_order").click()
    '''
    time.sleep(2)
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    
    driver.switch_to_window(window_after)
    driver.find_element_by_xpath("//div/div/div[@class='title_btn']").click()
    
    driver.switch_to_window(window_before)
    '''
    

driver = webdriver.Chrome('../../bin/chromedriver')
driver.implicitly_wait(3)

id_list = #
pw_list = #
login(id_list[0], pw_list[0])
while(True) :
    sys.stdout.flush()
    x = input('Enter mode : ')
    if(x == '3') :
        print('exit')
        break
    elif(x == '0') :
        sys.stdout.flush()
        login_number = int(input('login number : '))
        login(id_list[login_number], pw_list[login_number])
    elif x[0] == '5' :
        purchase(True, x[1]=='2')
    elif x == '10' :
        purchase()
    else:
        print("wrong input")

