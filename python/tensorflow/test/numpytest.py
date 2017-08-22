#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 21:38:37 2017

@author: mat
"""

import numpy as np
import math
import random
import pandas as pd
"""
arr = np.random.randint(0,10,size=(5,5))
arr1 = np.random.randint(0,10,size=(5,5))
s=arr.mean(axis=1)
p = arr - s[:,np.newaxis]
f= arr.dot(arr1)
"""

arr = np.random.randint(-10,10,size=(5,5))
arr1 = np.random.randint(0,10,size=(5,5))
arr2 = np.argsort(-arr,axis=1)
s = np.nonzero(arr)

def change(arr):
    p,q = arr.shape
    arr3 = np.ones((p,q))
    for i in range(p):
        for j in range(q):
            arr3[i][j] = 0
    return arr3



"""
arr = np.array([10 for x in range(10)])
arr1 =arr[:,np.newaxis]
"""