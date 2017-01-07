#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:42:44 2017

@author: ktt
"""

def prime_factors(n):
    m = n
    factors = [] 
    k = 2
    while m > 1:
        while m%k==0:
            factors.append(k)
            m /= k
        k += 1
    return factors