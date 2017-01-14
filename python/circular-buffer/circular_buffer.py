#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:33:31 2017

@author: ktt
"""

class CircularBuffer(object):
    
    def __init__(self, n):
        self.n = n # n is predefined length of buffer
        self.buffer = ['' for _ in range(n)] # creates blank list of len n
BufferFullException
BufferEmptyException