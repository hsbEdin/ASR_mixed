#! /usr/bin/env python3
#coding:utf-8

import sys
import jieba
#from __future__ import print_function

for line in sys.stdin:
    seg_list = ' '.join(jieba.cut(line, HMM=False))
    seg_list = seg_list.replace("  ", "")
    seg_list = seg_list.replace(" _ ", "_")
    print(seg_list)
