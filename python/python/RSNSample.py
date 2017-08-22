# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 21:03:56 2017

@author: Administrator
"""
import random

def RandomSelectNegativeSample(items_pool, items):
    """
    items_pool 传入样本候选集，传入方法为creatItems_pool
    items 对于用户x选择过的物品集
    """
    
    #重新构建items集
    ret = dict()
    for i in items.keys():
        ret[i] = 1
    n = 0
    for i in range(0, len(items)*3):
        item = items_pool[random.randint(0,len(items_pool) -1)]
        if item in ret:
            continue
        ret[item] = 0
        n += 1
        if n > len(items):
            break
        return ret
    

def creatItems_pool(item,rate):
    """
    设计思路：
    item 为所有用户选择的物品集
    rate 热度比率0-1，即归一化后排序，前rate部分组成候选集
    
    
    统计每个物品出现的次数
    m = x/max 计算每个物品的热度
    n 为用户选择物品的最大值
    m*100构建候选集
    """