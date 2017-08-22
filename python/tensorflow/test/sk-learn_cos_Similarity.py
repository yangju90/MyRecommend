#!/usr/bin/env python
#coding:utf-8

import numpy as np
import pandas as pd
import time
from sklearn import cross_validation as cv
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt

def read_file():

    header = ['user_id', 'item_id', 'rating', 'timestamp']
    df = pd.read_csv("/home/mat/ml-100k/u.data",sep = '\t',names = header)
    #去重之后得到一个元祖，分别表示行与列,大小分别为943与1682
    n_users = df.user_id.unique().shape[0]
    n_items = df.item_id.unique().shape[0]
    
    print('all users is :' + str(n_users) + ', all items is :' + str(n_items))

    #将样本分为训练集与测试机
    train_data,test_data = cv.train_test_split(df,test_size = 0.25)

    train_data_matrix = np.zeros((n_users,n_items))
    for line in train_data.itertuples():
        train_data_matrix[line[1]-1, line[2]-1] = line[3]

    test_data_matrix = np.zeros((n_users,n_items))
    for line in test_data.itertuples():
        test_data_matrix[line[1]-1,line[2]-1] = line[3]

    #计算user相似矩阵与item相似矩阵,大小分别为943*943,1682*1682
    user_similar = pairwise_distances(train_data_matrix, metric = "cosine")
    item_similar = pairwise_distances(train_data_matrix.T, metric = "cosine")

    return (train_data_matrix,test_data_matrix,user_similar,item_similar)

train_data_matrix,test_data_matrix,user_similar,item_similar = read_file()
print('user_similar.shape is :',user_similar.shape)
print('item_similar.shape is :',item_similar.shape)

def predict(rating, similar, type = 'user'):
    if type == 'user':
        #打分平均值
        #out0 
        """
        #mean_user_rating = rating.mean(axis = 1)
        """
        #out2
        mean_user_rating_molecule = rating.sum(axis = 1)
        mean_user_rating_denominator = []
        for line in rating:
            mean_user_rating_denominator.append(np.count_nonzero(line))
        mean_user_rating = mean_user_rating_molecule/mean_user_rating_denominator*1.0
        
        
        #out0,1

        rating_diff = rating - mean_user_rating[:,np.newaxis]

        #out1

        for i in range(len(rating_diff)):
            rating_diff[i] = [ 0 if x == -mean_user_rating[i] else x for x in rating_diff[i]]

        #.dot() martix mul not equals *
        #out0
        """
        pred = mean_user_rating[:,np.newaxis] + similar.dot(rating_diff) / np.array([np.abs(similar).sum(axis=1)]).T
        """
        #out3
        
        coord =np.argsort(-similar,axis=1)
        #选择top10的相似
        similar_10 = np.zeros(similar.shape)
        denominator = [10 for x in range(len(coord))]
        for i in range(len(coord)):
            for j in range(10):
                similar_10[i,coord[i][j]] = similar[i,coord[i][j]]

        div_pred = similar_10.dot(rating_diff)/np.array(denominator)[:,np.newaxis]
        for i in range(len(div_pred)):
            div_pred[i] = [ 0 if x == 0 else x + mean_user_rating[i] for x in div_pred[i]]
        pred = div_pred   
          
    elif type == 'item':
        pred = rating.dot(similar) / np.array([np.abs(similar).sum(axis=1)])

    return pred

user_prediction = predict(train_data_matrix, user_similar, type = 'user')
item_prediction = predict(train_data_matrix, item_similar, type = 'item')

def rmse(prediction,ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))

def rmse2(prediction,ground_truth):
    print(np.count_nonzero(prediction))
    p = []
    g = []
    with open('/home/mat/Desktop/python/work_out/mm.a','a') as f:
        for i in range(943):
            for j in range(1682):
                if prediction[i,j]!=0 and ground_truth[i,j] !=0 :
                    p.append(prediction[i,j])
                    g.append(ground_truth[i,j])
                    f.write('%s,%s,%f\n'%(prediction[i,j],ground_truth[i,j],prediction[i,j]-ground_truth[i,j]))
    prediction = np.array(p)
    ground_truth = np.array(g)
    print(np.count_nonzero(prediction))
    return sqrt(mean_squared_error(prediction, ground_truth))

print('User based CF RMSE: ' + str(rmse2(user_prediction, test_data_matrix)))
print('Item based CF RMSe: ' + str(rmse2(item_prediction, test_data_matrix)))
