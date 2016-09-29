# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 20:16:29 2016

@author: Ken
"""
import re

def decode(compressed, data=''):
    if len(compressed) == 0: #if nothing left to decode, return data
        return data
    else:
        d_pattern = re.compile(r'^(\d+)') # Any string of digits to start the str
        l_pattern = re.compile(r'^[a-zA-Z]{1}') # Only one letter at start of str
        d = re.findall(d_pattern, compressed)
        l = re.findall(l_pattern, compressed)
        if l:
            data += str(l[0]) # Appending single letter to decoded
            compressed = compressed[1:] # Removing the letter from compressed
            decode(compressed, data)
        elif d:
            data += str(int(d[0])*compressed[len(str(d[0]))])
            compressed = compressed[(len(str(d[0])) + 1):] # Remove len of number and letter
            decode(compressed, data)
