#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import SplitData as sd
import math
import evaluate as elu

#实现推荐算法p63

def Similarity(s,type ='user'):
    item_users ={}
    #训练集转换为物品对用户的dict
    if type == 'user':
        for l in s:
            if l[1] not in item_users:
                item_users[l[1]] = set()
            item_users[l[1]].add(l[0])
            
    elif type == 'item':
        for l in s:
            if l[0] not in item_users:
                item_users[l[0]] = set()
            item_users[l[0]].add(l[1]) 

    C = dict()
    N = dict()
    #计算相似度
    for i,users in item_users.items():
        for u in users:
            if u not in N.keys():
                N[u] = 0
            N[u] += 1
            for v in users:
                if u == v:
                    continue
                if u not in C.keys():
                    C[u] = dict()
                if v not in C[u].keys():
                    C[u][v] = 0
                #C[u][v] += 1
                C[u][v] += 1/math.log(1+len(users))

    W = dict()
    for u in C.keys():
        if u not in W.keys():
            W[u] = dict()
        for v,value in C[u].items():
            W[u][v]= (C[u][v]*1.0)/math.sqrt(N[u]*N[v])

    return W

#针对每个用户推荐
def Recommend(user,train,W,k,type = 'user'):
    rank = dict()
    interacted_items = train[user]
    if type == 'user':
        for v,Wuv in sorted(W[user].items(),key=lambda x:x[1],reverse=True)[0:k]:
            for i in train[v]:
                if i in interacted_items:
                    continue
                if i not in rank.keys():
                    rank[i] = 0
                rank[i] += Wuv
    elif type == 'item':
        for i in train[user]:
            for v,Wuv in sorted(W[i].items(),key=lambda x:x[1],reverse=True)[0:k]:
                if v in interacted_items:
                    continue
                if v not in rank.keys():
                    rank[v] = 0
                rank[v] += Wuv
    return rank
            

#将数据转换为 用户-物品集
def trfU2I(train):
    out = dict()
    for l in train:
        if l[0] not in out.keys():
            out[l[0]] = set()
        out[l[0]].add(l[1])
    return out

#函数对矩阵的行进行倒排并截取前k个
#取得每行最大的k个值
def martixSortAndSplit(W,k):
    out = dict()
    out_no_value = dict()
    for u in W.keys():
        out[u] = dict()
        out_no_value[u] = set()
        for i,value in sorted(W[u].items(),key=lambda x:x[1],reverse=True)[0:k]:
            out[u][i] = value
            out_no_value[u].add(i)
            
    return out,out_no_value

def run_ucf(u_k,i_k,type):
    """
    #读取数据
    data = sd.readfile(r'/home/mat/ml-100k/u.data')
    #划分训练集和测试集
    train,test = sd.SplitData(data,8,0,1)
    """
    train = sd.readfile_csv(r'E:/Recommend System/workspace/train.csv')
    test = sd.readfile_csv(r'E:/Recommend System/workspace/test.csv')
    
    
    W = Similarity(train,type)
            
    train_U2I = trfU2I(train)
    
    #计算推荐矩阵
    work_out = dict()
    for i in train_U2I.keys():
        user_rec = Recommend(i,train_U2I,W,u_k,type)
        work_out[i] = user_rec
    
    #输出推荐的前10位
    result,result_no_value = martixSortAndSplit(work_out,i_k)
    
    
    test_U2I = trfU2I(test)
    
    precision,recall = elu.precisionAndRecall(result_no_value,test_U2I)
    coverage = elu.coverage(train_U2I,result_no_value)
    
    popularity,novel = elu.popularityAndNovel(train_U2I,result_no_value)

    """
    with open('/home/mat/Desktop/python/work_out/User_S_10_160.csv','a') as f:
        #f.write('u_k,i_k,precision,recall,coverage,popularity,novel\n')
        f.write('%d,%d,%s,%s,%s,%s,%s\n'%(u_k,i_k,precision,recall,coverage,popularity,novel))
    """
    print(u_k,i_k,precision,recall,coverage,popularity,novel)

run_ucf(40,10,'item')
        
