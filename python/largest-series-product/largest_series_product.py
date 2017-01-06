#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Thu Jan  5 19:53:41 2017

@author: ktt
"""

import operator
from functools import reduce

# Series is string, num is int

def largest_product(series, num):
    w_moves = len(series) - num # number of times the window moves
    if num > w_moves + num:
        raise ValueError
    if num < 0:
        raise ValueError
    products = []
    for k in range(w_moves+1):
        s_num = series[k:k+num]
        products.append(reduce(operator.mul, [int(digit) for digit in s_num], 1))
    return max(products)