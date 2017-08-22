#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tensorflow as tf
a = tf.constant('hello,world!')
with tf.Session() as sess:
    print(sess.run(a))
