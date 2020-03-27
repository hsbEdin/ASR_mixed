#coding=utf-8

import sys
import re
import pandas as pd
import os

lists = []
count = 0
with open('./dict_out.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lists.append(line)
with open('./dict_out_count.txt', 'a+') as f1:
    with open('./c_500_out.txt', 'r') as f2:
        for line in f2.readlines():
            line = line.strip('\n')
            line = line.split('\t')
            if line[0] not in lists:
                f1.write(line[0]+'\n')
                count+=1
print(count)
# with open('./dict_in.txt','r') as f:
#     for line in f.readlines():
#         line = line.strip('\n')
#         print(line[:-4])
#         count += 1
#         if count==4:
#             break
        #lists.append(line)
#
# fore = "./"
# for way in lists:
#     path = fore+way
#     if os.path.exists(path):
#         os.remove(path)
