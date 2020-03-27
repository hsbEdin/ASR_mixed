#coding=utf-8

import sys
import os

with open("name_list.txt", "r") as f:  # 打开文件
    data = f.read().split(' ')
    data[-1] = 'G2415'

step = 0
count = 0
with open("TRANS.txt", "r") as f0:  # 打开文件
    for line in f0.readlines():
        if step == 0:
            step = 1
            continue
        line1 = line.strip('\n')
        line2 = line.split('\t')
        if line2[1][5:10] in data:
             with open('datain.txt','a+') as f1:
                f1.write(line)
        else:
             with open('dataout.txt','a+') as f2:
                f2.write(line)

    #for name in data:
