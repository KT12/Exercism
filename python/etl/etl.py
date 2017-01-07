#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:13:44 2017

@author: ktt
"""

def transform(old):
    # old is dict of {1: ['UPPER', 'UP']}
    # want to yield dict of {'upper' : 1, 'up' : 1}
    return {word.lower(): points for points, text in old.items() 
            for word in text}