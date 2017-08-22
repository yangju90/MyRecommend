# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 23:16:43 2017

@author: Administrator
"""
import math
import pandas as pd



def trfU2I_n(train):
    out = dict()
    for line in train.itertuples():
        if line[1] not in out.keys():
            out[line[1]] = set()
        out[line[1]].add(line[2])
    return out


#传入推荐集和测试集
def precisionAndRecall(rec,test):
    hit = 0
    allrecall = 0
    allprecision = 0
    for user in rec.keys():
        if user in test.keys():
            tu = test[user]
        else:
            tu = set()
        for i in rec[user]:
            if i in tu:
                hit += 1
        allrecall += len(tu)
        allprecision += len(rec[user])
    return hit/(allprecision*1.0),hit/(allrecall*1.0)


#传入训练集和推荐集
def coverage(train,rec):
    recommend_items = set()
    all_items = set()
    for user in train.keys():
        for i in train[user]:
            all_items.add(i)
    for user in rec.keys():
        for i in rec[user]:
            recommend_items.add(i)
    return len(recommend_items)/(len(all_items)*1.0)
    
def popularityAndNovel(train,rec):
    item_popularity = dict()
    item_novel = dict()
    flag = 0
    total = 0

    for user,items in train.items():
        for i in items:
            if i not in item_popularity:
                item_popularity[i] = 0
            item_popularity[i] += 1
            total += 1
            if flag<item_popularity[i]:
                flag = item_popularity[i]
    
    for i,item in item_popularity.items():
        item_novel[i] = 1 - item/flag*0.1

    ret_popul = 0
    ret_novel = 0
    n = 0
    for user in rec.keys():
        for i in rec[user]:
            ret_popul += math.log(1+ item_popularity[i])            
            ret_novel += item_novel[i]
            n += 1
    ret_popul /= n*1.0
    ret_novel /= n*1.0

    return ret_popul,ret_novel

header = ['user_id', 'item_id']
df_train = pd.read_csv("E:/Recommend System/train.csv",sep = ',',names=header)
df_test = pd.read_csv("E:/Recommend System/test.csv",sep = ',',names=header)
df_out = pd.read_csv("E:/Recommend System/python/work_out/sklearn_User10_item10.csv",sep = ',',names=header)
train = trfU2I_n(df_train)
out = trfU2I_n(df_out)
test = trfU2I_n(df_test)

precision,recall = precisionAndRecall(out,test)
cov = coverage(train,out)
pop,novel = popularityAndNovel(train,out)

print(precision,recall,cov,pop,novel)