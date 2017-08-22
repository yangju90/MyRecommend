#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 22:09:10 2017

@author: mat
"""

with open('/home/mat/Desktop/python/work_out/User_S.out','r') as f:
    flag  = True
    for line in f.readlines():
        if flag == True:
            flag = False
            continue
        l = line.split(',')[0:5]
        
        out  = float(l[2])*0.5+float(l[3])*0.5
        print(l[0],':',l[1],'-',out)