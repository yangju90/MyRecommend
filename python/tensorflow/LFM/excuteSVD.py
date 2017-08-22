# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 22:35:38 2017

@author: Administrator
"""
from SVD import *
from Data import *
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt


def rmse(prediction,ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))




with open('E:/Recommend System/python/tensorflow/LFM/out1.txt','a') as f:
    s = MF(min=1,max=5)

    s.load_data('E:/Recommend System/python/tensorflow/LFM/train.csv', sep = ',',format={'row':0, 'col':1, 'value':2, 'timespace':3})


    check_matrix = np.zeros((944,1683))
    lines = pd.read_csv('E:/Recommend System/python/tensorflow/LFM/check.csv', ',', header=None)
    for line in lines.itertuples():
        check_matrix[line[1], line[2]] = line[3]
    #for x in [10,20,40,60,80,100,160,200,250,300,400,500,600,800,1000]:
    i,p,e = s.factorize(check_matrix,k=500,iter=400,alpha=0.001,remeda=0.05,descent=False,descent_rate=0.9,pp=False)
    #f.write('%s%s%s\n'%(x,i,p))
    test_matrix = np.zeros((944,1683))
    lines = pd.read_csv('E:/Recommend System/python/tensorflow/LFM/test.csv', ',', header=None)
    for line in lines.itertuples():
        test_matrix[line[1], line[2]] = line[3]
    n = rmse(e,test_matrix)

"""
pre_matrix = np.zeros((944,1683))
for i in range(944):
    for j in range(1683):
        pre_matrix[i,j] = s.predict(i,j)


n = rmse(pre_matrix,test_matrix)
"""