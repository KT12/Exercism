# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:49:30 2016

@author: Ken
"""

from re import search

def is_pangram(string):
    string = filter(lambda c: search(r'[a-z]', c), string.lower())
    return len(set(string)) == 26