# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:44:43 2019

@author: ghost
"""

def parse_text(text_file) :
    coupon_list = []
    with open(text_file, "r", encoding='euc-kr') as f:
        for line in f.readlines():
            if line.startswith("쿠폰번호 : ") :
                single_coupon = line.replace("쿠폰번호 : ", '').replace('\n', '')
                coupon_list.append(single_coupon)
            elif line.startswith("* 쿠폰번호 : ") :
                single_coupon = line.replace("* 쿠폰번호 : ", '').replace("-", '').replace('\n', '')
                coupon_list.append(single_coupon)
    return coupon_list

raw_file_path = "./raw_product_text.txt"
parsed_file_path = "./parsed_product_text.txt"

coupon_list = parse_text(raw_file_path)

with open(parsed_file_path, "w") as f:
    count = 0
    for coupon in coupon_list : 
        f.write(coupon+'\n')
        print('purchased [{}]'.format(coupon))
        count += 1
        if count % 5 == 0 :
            f.write('\n')
    f.write('{} coupon \n'.format(str(count)))    
    print('total [{}] coupon parsed'.format(str(count)))