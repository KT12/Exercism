#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:13:44 2017

@author: ktt
"""
from math import sqrt

def encode(msg):
    if not msg:
        return ''
    
    # remove punct and lower the case
    clean   = ''.join(ch.lower() for ch in msg if ch.isalnum())
    
    # len of clean string
    st_len  = len(clean)
    
    # calc max length of each segment
    seg_len = int(round(sqrt(st_len), 0)) # should be int
    
    # calc num of segments needed
    if st_len%seg_len == 0:
        num_s = int(st_len/seg_len) # perfect sq
    else:
        num_s = int(st_len//seg_len + 1) # not a sq
    
    # create empty strings to add each letter to
    encoded = ['' for _ in range(num_s)]
    
    # use modulo to determine which string to add letter to
    for k in range(st_len):
        encoded[(k%num_s)] = encoded[(k%num_s)] + clean[k]
    
    return ' '.join(encoded)