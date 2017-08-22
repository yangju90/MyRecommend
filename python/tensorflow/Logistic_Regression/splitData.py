# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 21:51:01 2017

@author: Administrator
"""

import numpy as np
import pandas as pd
import time
from sklearn import cross_validation as cv
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt

#根据时间划分测试训练集
def read_file_AcTime():

    header = ['user_id', 'item_id', 'rating', 'time','age','gender','occupation']
    df = pd.read_csv("E:/Recommend System/combine_noheader.csv",sep = ',',names = header)
    
    #对时间排序,得到排序的下标
    sort_out = np.argsort(df.time,axis = 0)
    df_mat = np.mat(df)
    
    l = []
    for i in range(len(sort_out)):
 
        l.append([df_mat[sort_out[i],0],df_mat[sort_out[i],1],df_mat[sort_out[i],2],df_mat[sort_out[i],4],df_mat[sort_out[i],5],df_mat[sort_out[i],6],df_mat[sort_out[i],3]])
    
    df = l
    return df

def read_file():

    header = ['user_id', 'item_id', 'rating', 'time','age','gender','occupation']
    df = pd.read_csv("E:/Recommend System/combine_noheader.csv",sep = ',',names = header)
    
    train_data,test_data = cv.train_test_split(df,test_size = 0.2)

    return train_data,test_data

train_data,test_data = read_file()
"""
with open('E:/Recommend System/train_combine_noheader.csv','w') as f1:
    with open('E:/Recommend System/test_combine_noheader.csv','w') as f2:
        num = 1
        for i in s:
            num += 1
            if num>8000:
                f2.write('%d,%d,%d,%d,%d,%d,%d\n'%(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            else:
                f1.write('%d,%d,%d,%d,%d,%d,%d\n'%(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
"""
with open('E:/Recommend System/train_combine_noheader_splitrating.csv','w') as f1:
    num = 0
    for line in train_data.itertuples():
        if line[3]<4 :
            f1.write('%d,%d,%d,%d,%d,%d\n'%(line[1],line[2],line[5],line[6],line[7],0))
        else:
            f1.write('%d,%d,%d,%d,%d,%d\n'%(line[1],line[2],line[5],line[6],line[7],1))
            num = num+1
    print(num)
with open('E:/Recommend System/test_combine_noheader_splitrating.csv','w') as f2:
    for line in test_data.itertuples():
        if line[3]<4 :
            f2.write('%d,%d,%d,%d,%d,%d\n'%(line[1],line[2],line[5],line[6],line[7],0))
        else:
            f2.write('%d,%d,%d,%d,%d,%d\n'%(line[1],line[2],line[5],line[6],line[7],1))
                
    
    
