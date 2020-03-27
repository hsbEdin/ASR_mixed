#!/usr/bin/env python3
import os
import sys
import re
def main(argv):
    for line in open(argv, encoding = "utf-8"):
        line = re.sub(r'\[\w\]', '', line)#去除[N|S]格式
        line = re.sub(r'[！？，：；。~—\s]', '', line)#去标点符号
        return line

if __name__ == "__main__":
   print(main(sys.argv[1]))
