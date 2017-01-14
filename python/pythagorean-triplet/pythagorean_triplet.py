#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:22:27 2017

@author: ktt
"""

# The function primitive_triplets should then use the formula above with b set
# to its argument and find all possible pairs (m,n) such that m>n, m-n is odd,
# b=2*m*n and m and n are coprime.

import math

def primitive_triplets(b):
    if b%4 != 0:
        raise ValueError
    else:
        triplets = []
        for m in range(1, b//2 + 2):
            for n in range(1, m+2):
                if b == (2*m*n) and m>n and (m-n)%2 == 1 and math.gcd(m, n)==1:
                    a = m**2 - n**2
                    c = m**2 + n**2
                    if is_triplet([a,b,c]):
                        d,e,f = sorted([a, b, c])
                        triplets.append((d,e,f))
    return set(triplets)
    
def triplets_in_range(m, n):
    # Brute force
    triplets = set()
    for a in range(m, n-1):
        for b in range(a, n):
            for c in range(b+1, n+1):
                if a**2 + b**2 == c**2:
                    triplets.add((a,b,c))
    return triplets
        

def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return a**2 + b**2 == c**2