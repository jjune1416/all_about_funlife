# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:00:14 2019

@author: ghost
"""

from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.webdriver.support.ui as ui
import time
import sys

def login(id,pw):
    driver.get('https://signinssl.gmarket.co.kr/LogIn/LogIn')
    
    wait.until(lambda driver: driver.find_element_by_id("id"))
    id_cont = driver.find_element_by_id("id")
    id_cont.clear()
    id_cont.send_keys(id)
    
    pw_cont = driver.find_element_by_id("pwd")
    pw_cont.clear()
    pw_cont.send_keys(pw)
    
    driver.find_element_by_class_name('btn-login').click()
    
def logout() :
    driver.get('http://www.gmarket.co.kr/')
    wait.until(lambda driver: driver.find_element_by_class_name('logout'))
    driver.find_element_by_class_name('logout').click()
    time.sleep(1)
    print("logout")
    

def wait_and_switch_window() :
    try :
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException :
        return False
    return True

def purchase(purchase_5 = False, purchase_double = False) :
    url_funlife_10 = 'http://item.gmarket.co.kr/detailview/item.asp?goodscode=1561014051'
    url_funlife_5 = 'http://item.gmarket.co.kr/detailview/item.asp?goodscode=1561014990'

    if purchase_5 :
        print("purchase 5")
        driver.get(url_funlife_5)
    else :
        print("purchase 10")
        driver.get(url_funlife_10)
    
    wait.until(lambda driver: driver.find_element_by_id('coreInsOrderBtn'))
    time.sleep(1)
    if purchase_double :
        driver.find_element_by_class_name("bt_increase").send_keys(' ')
    
    driver.find_element_by_id("coreInsOrderBtn").send_keys(' ')
    
    wait.until(lambda driver: driver.find_element_by_id('shipping_option1'))
    buyer_name_cont = driver.find_element_by_id("shipping_option1")
    buyer_name_cont.clear()
    buyer_name_cont.clear()
    time.sleep(0.3)
    buyer_name_cont.send_keys('백인준')

    #phone_middle_cont = driver.find_elements_by_class_name("ng-pristine")[3]
    phone_middle_cont = driver.find_elements_by_xpath("//div/div/div/div/div/dl/dd/input")[1]
    phone_middle_cont.clear()
    phone_middle_cont.clear()
    time.sleep(0.3)
    phone_middle_cont.send_keys('6409')

    phone_last_cont = driver.find_elements_by_xpath("//div/div/div/div/div/dl/dd/input")[2]
    phone_last_cont.clear()
    phone_last_cont.clear()
    time.sleep(0.3)
    phone_last_cont.send_keys('9696')
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    driver.find_element_by_id('pay_type8').send_keys(' ')
    driver.find_element_by_id('pay_type2').send_keys(' ')
    driver.find_element_by_xpath("//select[@id='payCredit3']/option[@value='현대카드']").click()
    driver.find_element_by_id('use_point').send_keys(' ')
    
    driver.execute_script("window.scrollTo(0, 0);")
    
    '''
    
    #driver.find_element_by_class_name("btn_order").click()
    
    time.sleep(2)
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    
    driver.switch_to_window(window_after)
    driver.find_element_by_xpath("//div/div/div[@class='title_btn']").click()
    
    driver.switch_to_window(window_before)
    '''
    
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=caps, executable_path = '../../bin/chromedriver')
driver.implicitly_wait(3)

wait = ui.WebDriverWait(driver,10)

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
        logout()
        login(id_list[login_number], pw_list[login_number])
    elif x[0] == '5' :
        purchase(True, x[1]=='2')
    elif x == '10' :
        purchase()
    else:
        print("wrong input")
