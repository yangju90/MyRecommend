#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 09:49:03 2017

@author: mat
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']#设置显示中文

#生成曲线上的各个点
dataMat = np.loadtxt(open("/home/mat/Desktop/python/work_out/User_S_160_10.csv","r"),delimiter=",",skiprows=1)

trandata=np.transpose(dataMat)
xa=trandata[0]
ya=trandata[2]
yb=trandata[3]
yc=trandata[4]

plt.figure(1)
plt.ylim(ymax=1,ymin=0)

plt.title('user(x-160)-item10')
plt.xlabel('user_similarity')
plt.ylabel('probability')
#

plt.annotate("red:precision",xy =(120,0.92),color='r',fontsize=12)
plt.annotate("cyan:recall",xy =(120,0.85),color='c',fontsize=12)
plt.annotate("red:coverage",xy =(120,0.78),color='b',fontsize=12)
plt.plot(xa,ya,'r')
plt.plot(xa,yb,'c')
plt.plot(xa,yc,'b')

dataMat = np.loadtxt(open("/home/mat/Desktop/python/work_out/User_S_10_160.csv","r"),delimiter=",",skiprows=1)

trandata=np.transpose(dataMat)
xa=trandata[1]
ya1=trandata[2]
yb1=trandata[3]
yc1=trandata[4]

plt.figure(2)
plt.ylim(ymax=1,ymin=0)

plt.title('user10-item(x-160)')
plt.xlabel('item_similarity')
plt.ylabel('probability')
#

plt.annotate("red:precision",xy =(120,0.92),color='r',fontsize=12)
plt.annotate("cyan:recall",xy =(120,0.85),color='c',fontsize=12)
plt.annotate("red:coverage",xy =(120,0.78),color='b',fontsize=12)
plt.plot(xa,ya1,'r')
plt.plot(xa,yb1,'c')
plt.plot(xa,yc1,'b')

plt.show()
