# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:51:36 2017

@author: Administrator
"""
import RSNSample as rs

def LatentFactorModel(user_items,F ,N ,alpha , lam):
    [P,Q] = InitModel(user_items,F)
    for step in range(0,N):
        for user, items in user_items.items():
            samples = rs.RandomSelectNegativeSampleRandSelectNegativeSample(item_pool,items)
            
    