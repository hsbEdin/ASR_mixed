import re

with open('./text.txt','r', encoding='utf-8') as f:
    for line in f.readlines():

        line = line.replace('[SPK] ', '')
        line = line.replace('[SPK]', '')
        line = line.replace('[FIL] ', '')
        line = line.replace('[FIL]', '')
        with open('./new_text.txt','a+', encoding='utf-8') as f2:
            f2.write(line)
