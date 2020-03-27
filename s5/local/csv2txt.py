#coding=utf-8

import sys
import re
import pandas as pd
import os

data = pd.read_csv('./ce_20_dev.csv', encoding='utf-8')

with open('./TRANS.txt','a+', encoding='utf-8') as f:
    f.write('UtteranceID'+'\t'+'SpeakerID'+'\t'+'Transcription'+'\n')
    for line in data.values:
        line[0] = str(line[0])
        line[0] += '.wav'

        line[1] = str(line[1])
        line[1] = re.sub(r'data(.*)01/', '', line[1]).split('_')[0]

        line[2] = str(line[2])
        line[2] = re.sub(r'\[\w\]\s', '', line[2])#去除[N|S]格式
        line[2] = re.sub(r'\[\w\]', '', line[2])#去除[N|S]格式
        line[2] = line[2].replace('[SPK] ', '')
        line[2] = line[2].replace('[SPK]', '')
        line[2] = line[2].replace('[FIL] ', '')
        line[2] = line[2].replace('[FIL]', '')
        line[2] = re.sub(r'[！？，：；。]', '', line[2])#去标点符号
        line[2] = re.sub(r'[!?,;:。]', '', line[2])#去标点符号
        line[2] = re.sub(r'[\-]', ' ', line[2])#‘-‘转换为空格
        line[2] = re.sub(r'　', ' ', line[2])#不合法的空格

        #处理~APP词汇
        pattern = re.compile(r"[a-zA-Z][\u4e00-\u9fa5]")
        pattern1 = re.compile(r"[a-zA-Z][\u4e00-\u9fa5]")
        word = line[2].split('~')
        n = len(word)
        for i in range(1,n):
            tmp = [m.start() for m in re.finditer(pattern, word[i])]
            if tmp:
                position = [m.start() for m in re.finditer(pattern, word[i])][0]+1
                word[i] = " "+" ".join(word[i][:position])+" "+word[i][position:]
            else:
                word[i] = " "+" ".join(word[i])
        line[2] = "".join(word)

        #用空格分隔开英文+中文
        pattern = re.compile(r"[a-zA-Z][\u4e00-\u9fa5]")
        a = [m.start() for m in re.finditer(pattern, line[2])]
        a.reverse()
        line[2] = list(line[2])
        for i in a:
            line[2].insert(i+1, " ")
        f.write(line[0]+'\t'+line[1]+'\t'+"".join(line[2])+'\n')

#压缩成tar.gz
# tar -zcvf test.tar.gz test
# test.tar.gz 是将要压缩的名称
# test是你当前的文件 or 文件夹的名称
