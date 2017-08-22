#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:48:34 2017

@author: mat
"""
import tensorflow as tf

x = tf.Variable(3)
y = tf.Variable(4)
z = x+y
init  = tf.global_variables_initializer()
#init  = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(z))
