# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:41:35 2019

@author: ghost
"""
TEST_MODE = 0

import time
import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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

def purchase_one_product(p_name, f_driver):
    try:
        f_driver.find_element_by_partial_link_text(p_name).click()
        print('found {}'.format(p_name))
    except KeyboardInterrupt :
        sys.exit(1)
    except :
        return False

    product_url = f_driver.current_url
    print (product_url)
    begin = True
    while True :
        try :
            if begin :
                begin = False
            else :
                driver.get(product_url)
            
            order_count_elem = driver.find_element_by_id('order_count')
            order_count_elem.clear()
            order_count_elem.send_keys('5')
                
            f_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
            order_count_elem = f_driver.find_element_by_id('use_point')
            order_count_elem.clear()
            order_count_elem.send_keys('250000')
            
            f_driver.find_element_by_id('checkAll').send_keys(' ')
            time.sleep(0.5)
            f_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            f_driver.find_element_by_xpath("//div[@id='order_form']/div/div/button").click()
    
        except KeyboardInterrupt :
            sys.exit(1)
        except NoSuchElementException:
            return True
        except :
            continue
        print("purchased {}".format(p_name))
        
    return True

def auto_purchase() :
    loop_count = 0
    while True :
        found = False
        try :
            driver.get(product_list_url)
        except KeyboardInterrupt :
            sys.exit(1)
        except:
            continue
      
        for product_name in product_name_list :
            found = found or purchase_one_product(product_name, driver)
    
        loop_count += 1
        if loop_count % 10 ==  0 :
            print ("{} loop done".format(loop_count))

driver = webdriver.Chrome('../bin/chromedriver')
driver.implicitly_wait(3)

with open("./idpw.conf") as f:
    my_id = f.readline()
    my_pw = f.readline()

while(not login(my_id, my_pw)) : pass

product_list_url = 'http://my.funpass.co.kr/mall/shop/3'
product_name_list = ['해피머니']
if TEST_MODE :
    product_list_url = 'http://my.funpass.co.kr/mall/shopi/1'
    product_name_list = ['해피머니', '카페베네'] #test

print ('-product list.')
print (product_name_list)

auto_purchase()