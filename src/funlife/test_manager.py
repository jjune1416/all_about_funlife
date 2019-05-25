# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:39:45 2019

@author: ghost
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

import time
import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from multiprocessing import Pool, cpu_count

class Purchaser():
    
    def __init__(self, my_id, my_pw, product_url):
        self.driver = None
        self.product_url = product_url
        self.my_id = my_id
        self.my_pw = my_pw
    
    def login(self):
        try :
            self.driver.get('http://my.funpass.co.kr/users/login')
            id_cont = self.driver.find_element_by_id('user_id')
            id_cont.clear()
            id_cont.send_keys(self.my_id)
            pw_cont = self.driver.find_element_by_id('password')
            pw_cont.clear()
            pw_cont.send_keys(self.my_pw)
            self.driver.find_element_by_class_name('login_btn').click()
        except KeyboardInterrupt :
            sys.exit(1)
        except :
            return False
        try :
            self.driver.get('http://my.funpass.co.kr/mall/shop/3')
            self.driver.find_element_by_partial_link_text('로그인').click()
        except :
            return True
        return False

    def purchase_one_product(self, url):
        try :
            self.driver.get(url)            
            
            order_count_elem = self.driver.find_element_by_id('order_count')                
            order_count_elem.clear()
            order_count_elem.send_keys('5')                
            
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
            #f_driver.find_element_by_xpath('//tr/td/div/span/button').click()
            order_count_elem = self.driver.find_element_by_id('use_point')
            order_count_elem.clear()
            order_count_elem.send_keys('25')
            #order_count_elem.send_keys('250000')
            
            #f_driver.find_element_by_id('checkAll').click()
            self.driver.find_element_by_id('checkAll').send_keys(' ')
            time.sleep(0.5)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//div[@id='order_form']/div/div/button").click()
            
            #purchase_button = f_driver.find_element_by_xpath("//div[@id='order_form']/div/div/button")
            #purchase_button.send_keys(' ')
            #purchase_button.click()
            
        except KeyboardInterrupt :
            sys.exit(1)
        except NoSuchElementException:
            return True
        #except WebDriverException :
        #sys.exit(1)
        except :
            return False
        print("purchased {}".format(url))
        return True

    def run(self):
        self.driver = webdriver.Chrome('../bin/chromedriver')
        self.driver.implicitly_wait(3)
        
        #proc_name = self.name
        while(not self.login()) : pass
    
        while True:
            if not len(self.product_url) == 0 :
                self.purchase_one_product(self.product_url[0])
            time.sleep(0.1)
        return
    
    def start(self):
        self.driver = webdriver.Chrome('../bin/chromedriver')
        self.driver.implicitly_wait(3)
        
        #proc_name = self.name
        while(not self.login()) : pass
    
        while True:
            if not len(self.product_url) == 0 :
                self.purchase_one_product(self.product_url[0])
            time.sleep(0.1)
        return

def multi_processed(id, pw, url) :
    Purchaser.start(id, pw, url)
    
   
if __name__ == '__main__' :
    with open("./idpw.conf") as f:
        my_id = f.readline()
        my_pw = f.readline()
        
    with open("./product.conf") as f:
        product_name_list = f.readlines()

    purchaser_count = 2
    purchasers = []
    pool = Pool()
    
    threads = []
    product_url = []

    for i in range(purchaser_count) :
        print(i)
        purchaser = Purchaser(my_id, my_pw, product_url)
        #purchaser.start()
        purchasers.append(purchaser)
        time.sleep(3)
    for p in purchasers : p.start()
        

    while(True) :
        html = urlopen("http://my.funpass.co.kr/mall/shop/1")  
        bsObject = BeautifulSoup(html, "html.parser")
        links = bsObject.find_all('a')
        
        time.sleep(10)
        for link in links:
            if "갈비천왕" in link.text :
                print("found " + "갈비천왕")
                product_url.append("http://my.funpass.co.kr" + link.get('href'))
                time.sleep(10)
            else : # 다른것 찾아보기
                product_url.clear()

    for proc in threads:
        pool.close()
        pool.join()
