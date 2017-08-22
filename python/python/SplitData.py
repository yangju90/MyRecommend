#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

def readfile(s):
    data = []
    with open(s,'r') as f:
        for readline in f.readlines():
            r = readline.split()
            data.append([r[0],r[1],r[2],r[3]])
    return data

def readfile_csv(s):
    data = []
    with open(s,'r') as f:
        for readline in f.readlines():
            r = readline.split(',')
            data.append([r[0],r[1]])
    return data       

def SplitData(data, M, k, seed):
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0,M) == k:
            test.append([user,item])
        else:
            train.append([user,item])
    return train, test

def SplitData1(data, M, k,k1, seed):
    test = []
    train = []
    check = []
    random.seed(seed)
    for user, item,rating,tm in data:
        c= random.randint(0,M)
        if  c == k:
            test.append([user,item,rating,tm])
        elif c == k1:
            check.append([user,item,rating,tm])
        else:
            train.append([user,item,rating,tm])
    return train, test, check

def writefile(s,test): # s为写入路径 test为一个list文件
    with open(s,'w') as f:
        for t in test:
            f.write('%s,%s,%s,%s\n'%(t[0],t[1],t[2],t[3]))

"""
train,test = SplitData(data,8,0,1)

with open('E:/Recommend System/workspace/test.csv','w') as f:
    for t in test:
        f.write('%s,%s\n'%(t[0],t[1]))

with open('E:/Recommend System/workspace/train.csv','w') as f:
    for t in train:
        f.write('%s,%s\n'%(t[0],t[1]))
"""
    
data = readfile('E:/Recommend System/data/ml-100k/u.data')
train, test, check = SplitData1(data,10,1,2,3)
writefile('E:/Recommend System/python/tensorflow/LFM/train.csv',train)
writefile('E:/Recommend System/python/tensorflow/LFM/test.csv',test)
writefile('E:/Recommend System/python/tensorflow/LFM/check.csv',check)
    