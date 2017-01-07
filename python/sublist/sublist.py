#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:00:57 2017

@author: ktt
"""
EQUAL = 0
UNEQUAL = 1
SUPERLIST = 2
SUBLIST = 3

def check_lists(A, B):
    if A == B:
        return EQUAL
    elif A in check_permutations(B, len(A)):
        return SUBLIST
    elif B in check_permutations(A, len(B)):
        return SUPERLIST
    else:
        return UNEQUAL
        
def check_permutations(A, len_B):
    return [A[k:k+len_B] for k in range(len(A) - len_B + 1)]