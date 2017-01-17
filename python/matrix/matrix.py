#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:13:03 2017

@author: ktt
"""

import numpy as np

class Matrix(object):
    def __init__(self, unrolled):
        self.r = unrolled.split('\n')
        
        self.rows = [list(map(int, self.r[k].split()))
                    for k in range(len(self.r))]
        
        self.matrix = np.array(self.rows)
        
        self.columns = [list(self.matrix[:,k])
                    for k in range(self.matrix.shape[1])]