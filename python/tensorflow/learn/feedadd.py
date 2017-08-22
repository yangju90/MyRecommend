#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:05:27 2017

@author: mat
"""
import tensorflow as tf

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a,b)
mul = tf.multiply(a,b)

with tf.Session() as sess:
    print('a+b=',sess.run(add,feed_dict={a:2,b:3}))
    print('a*b=',sess.run(mul,feed_dict={a:2,b:3}))


