# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:27:23 2017

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(X):
    return 1.0/(1+np.exp(-X))

class logRegressClassifier(object):
    
    def __init__(self):
        self.dataMat = list()
        self.labelMat = list()
        self.weights = list()
        
    def loadDataSet(self, filename):
        fr = open(filename)
        for line in fr.readlines():
            lineArr = line.strip().split(',')
            dataLine = [1.0]
            for i in lineArr:
                dataLine.append(float(i))
            label = dataLine.pop()
            self.dataMat.append(dataLine)
            self.labelMat.append(int(label))
        self.dataMat = np.mat(self.dataMat)
        self.labelMat = np.mat(self.labelMat).transpose()
    
    def train(self):
        self.weights = self.stocGradAscent1()
        
    def batchGradAscent(self):
        m,n = np.shape(self.dataMat)
        alpha = 0.001
        maxCycles = 500
        weights = np.ones((n,1))
        for k in range(maxCycles):
            h = sigmoid(self.dataMat * weights)
            error = (self.labelMat - h)
            weights += alpha * self.dataMat.transpose()*error
        return weights
    
    def stocGradAscent1(self):
        m,n = np.shape(self.dataMat)
        alpha = 0.001
        weights = np.ones((n,1))
        for i in range(m):
            h = sigmoid(sum(self.dataMat[i] * weights))
            error = self.labelMat[i] -h
            weights += (alpha * error * self.dataMat[i]).transpose()
        return weights
            
        
    def stocGradAscent2(self):
        numIter = 2
        m,n = np.shape(self.dataMat)
        weights = np.ones((n,1))   #initialize to all ones
        for j in range(numIter):
            dataIndex = range(m)
            for i in range(m):
                alpha = 4/(1.0+j+i)+0.0001    #apha decreases with iteration, does not 
                randIndex = int(np.random.uniform(0,len(dataIndex)))#go to 0 because of the constant
                h = sigmoid(sum(self.dataMat[randIndex] * weights) )
                error = self.labelMat[randIndex] - h
                weights += (alpha * error * self.dataMat[randIndex]).transpose()
                del(dataIndex[randIndex])
        return weights
        
    def classify(self, X):
        prob = sigmoid(sum( X * self.weights))
        if prob > 0.5:
            return 1.0
        else: 
            return 0.0

    def test(self):
        self.loadDataSet('E:/Recommend System/train_combine_noheader_splitrating.csv')
        #weights0 = self.batchGradAscent()
        weights1 = self.stocGradAscent1()
        #weights2 = self.stocGradAscent2()
        #print('batchGradAscent:', weights0)
        print('stocGradAscent0:', weights1)
        #print('stocGradAscent1:', weights2)
        return weights1
        
if __name__ == '__main__':
    lr = logRegressClassifier()
    weights1 = lr.test()  
    lt = logRegressClassifier()
    lt.loadDataSet('E:/Recommend System/test_combine_noheader_splitrating.csv')
    s = lt.dataMat
    o = lt.labelMat
    m ,n = s.shape
    p = []
    p1 = []
    for i in range(m):
        sum = 0.0
        for j in range(n):
            sum = sum + s[i,j]*weights1[j,0]
        sum1 = sigmoid(sum)
        p1.append(sum1)
        if sum1<0.5:
            p.append(0)
        else:
            p.append(1)
    num = 0
    num1 = 0

    for  i in range(m):
        if o[i] == p[i]:
            num = num +1 
        if o[i] == 1:
            num1 = num1+1
    
            