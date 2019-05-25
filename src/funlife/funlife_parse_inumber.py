# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:44:43 2019

@author: ghost
"""

def parse_text(text_file) :
    coupon_list = []
    with open(text_file, "r") as f:
        for line in f.readlines():
            tokens = line.split(" ")
            if len(tokens) != 9 :
                continue
            if tokens[1] != "아이넘버" :
                continue
            coupon_number = tokens[5].replace('-','')
            coupon_list.append(coupon_number)
            print (tokens)
    return coupon_list

raw_file_path = "./inumber_table.txt"
parsed_file_path = "./parsed_inumber_text.txt"

coupon_list = parse_text(raw_file_path)

with open(parsed_file_path, "w") as f:
    count = 0
    for coupon in coupon_list : 
        f.write(coupon+'\n')
        print('parsed [{}]'.format(coupon))
        count += 1
        if count % 5 == 0 :
            f.write('\n')
        
    print('total [{}] coupon parsed'.format(str(count)))