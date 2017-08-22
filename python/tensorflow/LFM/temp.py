# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
import numpy as np
import math
import random
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt


def personalRatingCustom(s,k):
    lines = pd.read_csv(s, ',', header=None)
    test_matrix = np.zeros((943,1682))
    for line in lines.itertuples():
        test_matrix[line[1]-1, line[2]-1] = line[3]
    
    l = np.zeros((943,5))
    for i in range(943):
        d = collections.Counter(test_matrix[i])
        for j in range(5):
            if j+1 in d.keys():
                l[i][j] = d[j+1]
    l1 = np.zeros((943,4))
    
    for i in range(943):
        for j in range(4):
            if l[i][j] > k and l[i][j+1] > k:
                l1[i][j] = l[i][j]/(l[i][j]+l[i][j+1]) + 1+j
            else:
                l1[i][j] = j+1+0.5
    return l1

def processM(m,l):
    p,q = m.shape
    m1 = np.zeros((p,q))
    for f in range(p):
        for g in range(q):
            if m[f][g] >= 5:
                m1[f][g] = 5
                continue
            if m[f][g] <= 1:
                m1[f][g] = 1
                continue
            c = int(m[f][g])
            if l[f][c-1] > m[f][g]:
                m1[f][g] = c
            else:
                m1[f][g] = c+1
    return m1
    

