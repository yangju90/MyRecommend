#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def transformcsv(source,dest,listdemo):
    data = []
    """data.append(listdemo)"""
    with open(source,'r') as f:
        for readline in f.readlines():
            r = readline.split()
            data.append(r)
    with open(dest,'w') as f:
        for t in data:
            f.write('%s,%s,%s,%s\n'%(t[0],t[1],t[2],t[3]))

listdemo = ['user_id','item_id','rating','timestamp']  
transformcsv('E:/Recommend System/upload/u.data','E:/Recommend System/upload/u.csv',listdemo)
