#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:17:11 2017

@author: mat
"""
import tensorflow as tf

a = tf.Variable(tf.ones([3,2]))
b = tf.Variable(tf.ones([2,3])

product = tf.matmul(tf.multiply(5,a),tf.multiply(4,b))
#bianliangchushihua
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(product))

