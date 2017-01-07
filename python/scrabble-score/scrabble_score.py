#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:32:34 2017

@author: ktt
"""

pts = {'a' : 1,
       'e' : 1,
       'i' : 1,
       'o' : 1,
       'u' : 1,
       'l' : 1,
       'n' : 1,
       'r' : 1,
       's' : 1,
       't' : 1,
       'd' : 2,
       'g' : 2,
       'b' : 3,
       'c' : 3,
       'm' : 3,
       'p' : 3,
       'f' : 4,
       'h' : 4,
       'v' : 4,
       'w' : 4,
       'y' : 4,
       'k' : 5,
       'j' : 8,
       'x' : 8,
       'q' : 10,
       'z' : 10}

def score(word):
    if not word.isalpha():
        return 0
    else:
        return sum(pts[k] for k in word.lower())