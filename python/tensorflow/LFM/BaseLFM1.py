# -*- coding: utf-8 -*-

'''
本函数用来实现推荐系统里面的LFM算法，并且求出QR矩阵
运用梯度下降法来进行参数更新
'''

import numpy as np
import math
import random
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
import temp as te

def qr(k,learningRate,lamda_user,lamda_item,noOfIteration,file_training):
    '''

    :param k: 隐含的特征个数，其实就是将用户兴趣分成k类，将物品分成k类
    :param learningRate:在梯度下降更新参数过程中的学习率
    :param lamda_user:Pu的正则化参数
    :param lamda_item:Qr的正则化参数
    :param noOfIteration:最大迭代次数
    :param file_training:字符串；文件路径及文件名
    :return:
    '''
    maximumRating=0
    #lines = pd.read_csv(file_training, delim_whitespace=True, header=None)
    lines = pd.read_csv(file_training, ',', header=None)
    

    numberOfUsers=0
    numberOfItems=0
    userID=np.zeros((len(lines)))
    itemID=np.zeros((len(lines)))
    rating=np.zeros((len(lines)))
    count=0

    for i in range(len(lines)):
        userID[count] = int(lines.iloc[i][0])-1
        if userID[count]>(numberOfUsers-1):
            numberOfUsers = userID[count]+1
        itemID[count] = int(lines.iloc[i][1])-1
        if itemID[count]>(numberOfItems-1):
            numberOfItems= itemID[count]+1
        rating[count] = float(lines.iloc[i][2])
        if rating[count]>maximumRating:
            maximumRating = rating[count]
        count=count+1

    maximumRating=float(maximumRating)

    ####初始化LFM的矩阵P和矩阵Q，采用随机初化的办法进行初始化，以我的经验，这样比全零初始化更快达到最优。
    p=np.array([[float(random.uniform(0,math.sqrt(maximumRating/k))) for i in range(k)] for j in range(int(numberOfUsers))])
    q=np.array([[float(random.uniform(0,math.sqrt(maximumRating/k))) for i in range(k)] for j in range(int(numberOfItems))])
    

    
    ##利用梯度下降法更新参数
    """
    error=np.zeros((noOfIteration))
    """
    for i in range(noOfIteration):
        for j in range(len(lines)):
            p[int(userID[j]), :] = p[int(userID[j]), :] + learningRate * ((rating[j] -np.dot(p[int(userID[j]), :],q[int(itemID[j]), :])) * q[int(itemID[j]), :] - lamda_user * p[int(userID[j]), :])
            q[int(itemID[j]), :] = q[int(itemID[j]), :] + learningRate * ((rating[j] -np.dot(p[int(userID[j]), :],q[int(itemID[j]), :])) * p[int(userID[j]), :] - lamda_item * q[int(itemID[j]), :])
        """
        for j in range (len(lines)):
            error[i]= error[i] + math.pow(rating[j] - np.dot(p[int(userID[j]),:], q[int(itemID[j]),:]),2)

        error[i]=math.sqrt(error[i])/len(lines)
        """
    """
    return error,p,q
    """
    return p,q

def rmse(prediction,ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))


if __name__=='__main__':
    """
    with open('/home/mat/out1.txt','a') as f: 
        for i in [10,20,40,60,80,100,160,200,250,300,400]:
            (p,q)=qr(i, 0.02, 0.01, 0.01, 1000, '/home/mat/train.csv')
            test_matrix = np.zeros((943,1682))
            lines = pd.read_csv('/home/mat/test.csv', ',', header=None)
            for line in lines.itertuples():
                test_matrix[line[1]-1, line[2]-1] = line[3]
            m = np.dot(p,q.T)
            n = rmse(m,test_matrix)
            f.write('%s,%s\n' %(i,n))
            n1 = []
            for k in [0,1,3,6,10,15,20]:
                l = te.personalRatingCustom('/home/mat/train.csv',k)
                m1 = te.processM(m,l)
                n1.append(rmse(m,test_matrix))
            f.write('%s,%s,%s,%s,%s,%s,%s\n' %(n1[0],n1[1],n1[2],n1[3],n1[4],n1[5],n1[6])) 
        
    """
    (p,q)=qr(10, 0.02, 0.01, 0.01, 1000, 'E:/Recommend System/python/tensorflow/LFM/train.csv')
    test_matrix = np.zeros((943,1682))
    lines = pd.read_csv('E:/Recommend System/python/tensorflow/LFM/test.csv', ',', header=None)
    for line in lines.itertuples():
        test_matrix[line[1]-1, line[2]-1] = line[3]
    m = np.dot(p,q.T)
    n = rmse(m,test_matrix)
    """
    n1 = []

    for k in range(10):
        l = te.personalRatingCustom('E:/Recommend System/python/tensorflow/LFM/train.csv',k)
        m1 = te.processM(m,l)
        n1.append(rmse(m,test_matrix))
    """

        


    
    
    