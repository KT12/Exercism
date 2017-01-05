# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:37:43 2016

@author: Ken
"""

#==============================================================================
#   Run length encoding and decoding
#   Lossless method
#   "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
#   "AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
#==============================================================================

import re

def encode(data, compressed=''):
    if len(data) == 0:
        return compressed # Ultimately want to end up here
    else:
        char_pattern = re.compile(r'(.)\1*')
        m = re.search(char_pattern, data)
        run_count = len(m.group(0)) # Careful, int not str
        run_value = m.group(0)[0] # str
        if run_count == 1: # No need for '1' as prefix if single letter in group
            compressed += run_value
            data = data[run_count:]
            return encode(data, compressed)
        else:
            compressed = compressed + str(run_count) + run_value
            data = data[run_count:]
            return encode(data, compressed)
    


def decode(compressed, data=''):
    if len(compressed) == 0: #if nothing left to decode, return data
        return data
    else:
        d_pattern = re.compile(r'^(\d+)') # Any string of digits to start the str
        l_pattern = re.compile(r'^[a-zA-Z]{1}') # Only one letter at start of str
        s_pattern = re.compile(r'^(\s+)') # White space
        u_pattern = re.compile(r'^(.)\1*') # Normally catches anything, but only unicode left
        d = re.findall(d_pattern, compressed)
        l = re.findall(l_pattern, compressed)
        s = re.findall(s_pattern, compressed)
        u = re.findall(u_pattern, compressed)
        if l:
            data += str(l[0]) # Appending single letter to decoded
            compressed = compressed[1:] # Removing the letter from compressed
            return decode(compressed, data) # Originally forgot return here, didn't work
        elif d:
            data += str(int(d[0])*compressed[len(str(d[0]))])
            compressed = compressed[(len(str(d[0])) + 1):] # Remove len of number and letter
            return decode(compressed, data) # Originally forgot return here, didn't work
        elif s:
            data += str(s[0]) # Appending single letter to decoded
            compressed = compressed[1:] # Removing the letter from compressed
            return decode(compressed, data) # Originally forgot return here, didn't work
        elif u:
            data += str(u[0]) # Appending single letter to decoded
            compressed = compressed[1:] # Removing the letter from compressed
            return decode(compressed, data)
        else:
            raise Exception