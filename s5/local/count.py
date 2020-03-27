import sys
import re
import pandas as pd
import os

data = pd.read_csv('./ce_20_dev.csv', encoding='utf-8')
word_list = []
#pattern = re.compile(r"[^\~][A-Z][A-Z]+")
pattern = re.compile(r"[~][A-Z][A-Z]+")


for line in data.values:
    line[2] = str(line[2])
    list = [m for m in re.finditer(pattern, line[2])]
    for ele in list:
        word_list.append(line[2][ele.span()[0]:ele.span()[1]])

print(word_list)

#压缩成tar.gz
# tar -zcvf test.tar.gz test
# test.tar.gz 是将要压缩的名称
# test是你当前的文件 or 文件夹的名称
