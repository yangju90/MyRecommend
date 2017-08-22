# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:15:36 2017

@author: Administrator
"""


import numpy as np
import pandas as pd
import time
from sklearn import cross_validation as cv
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt

def similarity(train_data):
    train_denominator_temp = train_data.sum(axis=1)
    train_molecule = train_data.dot(train_data.T)
    for i in range(len(train_molecule)):
        train_molecule[i,i] = 0
    train_denominator = train_denominator_temp[:,np.newaxis].dot(train_denominator_temp[np.newaxis,:])
    similar = train_molecule/np.sqrt(train_denominator)
    return similar   
    

def read_file():
    header = ['user_id', 'item_id']
    df_train = pd.read_csv("E:/Recommend System/train.csv",sep = ',',names=header)
    df_test = pd.read_csv("E:/Recommend System/test.csv",sep = ',',names=header)
    #去重之后得到一个元祖，分别表示行与列,大小分别为943与1682
    n_users = df_train.user_id.unique().shape[0]
    n_items = df_train.item_id.unique().shape[0]
    
    print('all users is :' + str(n_users) + ', all items is :' + str(n_items))

    train_data_matrix = np.zeros((943,1682))
    for line in df_train.itertuples():
        train_data_matrix[line[1]-1, line[2]-1] = 1
    
    test_data_matrix = np.zeros((943,1682))
    for line in df_test.itertuples():
        test_data_matrix[line[1]-1,line[2]-1] = 1
    #计算user相似矩阵与item相似矩阵,大小分别为943*943,1682*1682
    user_similar = pairwise_distances(train_data_matrix, metric = "cosine")
    item_similar = pairwise_distances(train_data_matrix.T, metric = "cosine")
    
    #user_similar = similarity(train_data_matrix)
    
    return (train_data_matrix,test_data_matrix,user_similar,item_similar)

train_data_matrix,test_data_matrix,user_similar,item_similar = read_file()
print('user_similar.shape is :',user_similar.shape)
print('item_similar.shape is :',item_similar.shape)

def predict(rating, similar, user_topn = 10, item_topn = 10, type = 'user'):
    if type == 'user':       
        coord =np.argsort(-similar,axis=1)
        #选择top10的相似
        similar_10 = np.zeros(similar.shape)
        
        #保留Top10的相似度，其余部分设置为0
        for i in range(len(coord)):
            for j in range(user_topn):
                similar_10[i,coord[i][j]] = similar[i,coord[i][j]]        

        pred_div = similar_10.dot(rating)
        
        #获取非0坐标
        flat = rating.nonzero()
        
        m = 0
        for  i in range(len(flat[0])):
            if pred_div[flat[0][i],flat[1][i]] != 0:
               m +=1                 
            pred_div[flat[0][i],flat[1][i]] = 0

        coord2 = np.argsort(-pred_div,axis = 1)
        

        with open('E:/Recommend System/python/work_out/sklearn_User10_item10.csv','a') as f:
            for i in range(len(coord2)):
                for j in range(item_topn):
                    f.write('%d,%d\n'%(i+1,coord2[i][j]+1))

        pred = pred_div        
    elif type == 'item':
        pred = rating.dot(similar) / np.array([np.abs(similar).sum(axis=1)])

    return pred

user_prediction = predict(train_data_matrix, user_similar, type = 'user')
item_prediction = predict(train_data_matrix, item_similar, type = 'item')

