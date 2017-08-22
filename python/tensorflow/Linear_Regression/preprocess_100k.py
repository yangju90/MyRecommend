# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 00:04:10 2017

@author: Administrator
"""

def readfile(s,tag = ''):
    data = []
    with open(s,'r') as f:
        for readline in f.readlines():
            if tag == '':
                r = readline.split()
            else:
                r = readline.split(tag)
            l = []
            for i in range(len(r)):
                l.append(r[i])
            data.append(l)
    return data

def combine(s,v):
    m = []
    for l in range(len(s)):
        line = []
        for i in range(len(s[l])):
            line.append(int(s[l][i]))
        line.append(v[s[l][0]-1][1])
        line.append(v[s[l][0]-1][2])
        line.append(v[s[l][0]-1][3])    
        m.append(line)
        
    return m

udata_0 = readfile(r'E:\Recommend System\data\ml-100k\u.data')
uuser_0 = readfile(r'E:\Recommend System\data\ml-100k\u.user','|')

uuser_1 = []
#去除没有参考价值的邮编
for l in range(len(uuser_0)):
    line = []
    line.append(int(uuser_0[l][0]))
    line.append(int(uuser_0[l][1]))
    if uuser_0[l][2] =='M':
        line.append(0)
    else:
        line.append(1)
        
    if uuser_0[l][3] == 'administrator':
        line.append(0)
    elif uuser_0[l][3] == 'artist':
        line.append(1)
    elif uuser_0[l][3] == 'doctor':
        line.append(2)
    elif uuser_0[l][3] == 'educator':
        line.append(3)
    elif uuser_0[l][3] == 'engineer':
        line.append(4)
    elif uuser_0[l][3] == 'entertainment':
        line.append(5)
    elif uuser_0[l][3] == 'executive':
        line.append(6)
    elif uuser_0[l][3] == 'healthcare':
        line.append(7)
    elif uuser_0[l][3] == 'homemaker':
        line.append(8)
    elif uuser_0[l][3] == 'lawyer':
        line.append(9)
    elif uuser_0[l][3] == 'librarian':
        line.append(10)
    elif uuser_0[l][3] == 'marketing':
        line.append(11)
    elif uuser_0[l][3] == 'none':
        line.append(12)
    elif uuser_0[l][3] == 'other':
        line.append(13)
    elif uuser_0[l][3] == 'programmer':
        line.append(14)
    elif uuser_0[l][3] == 'retired':
        line.append(15)
    elif uuser_0[l][3] == 'salesman':
        line.append(16)
    elif uuser_0[l][3] == 'scientist':
        line.append(17)
    elif uuser_0[l][3] == 'student':
        line.append(18)
    elif uuser_0[l][3] == 'technician':
        line.append(19)
    elif uuser_0[l][3] == 'writer':
        line.append(20)
    uuser_1.append(line)
    
for l in range(len(udata_0)):
    line = []
    for i in range(len(udata_0[l])):
        line.append(int(udata_0[l][i]))
    udata_0[l] = line
 
c = combine(udata_0,uuser_1)       

with open('E:/Recommend System/workspace/combine.csv','a') as f:
    f.write('user_id,item_id,rating,time,age,gender,occupation\n')
    for t in c:
        f.write('%s,%s,%s,%s,%s,%s,%s\n'%(t[0],t[1],t[2],t[3],t[4],t[5],t[6]))
        
