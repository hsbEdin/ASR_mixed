import sys
import re
lists = {}
count_line = 1
with open("ce_200.txt", "r") as f:
    for line in f.readlines():
        line = line.split()[2]
        pattern = re.compile(r"[A-Z][A-Z]+")
        word = pattern.findall(line)
        if word:
            if len(word[0])<=3:
                lists[count_line]=word
        count_line+=1
print(lists)
