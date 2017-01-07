#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:08:10 2017

@author: ktt
"""

from string import ascii_lowercase

c = ascii_lowercase[3:] + ascii_lowercase[:3]
encode_table = str.maketrans(ascii_lowercase, c)
decode_table = str.maketrans(c, ascii_lowercase)

class Caesar(object):
    
    def __init__(self):
        pass
    
    def encode(self, ph):
        cipher = ph.lower().translate(encode_table)
        return cipher.strip(' ')
    
    def decode(self, ph):
        decoded = ph.translate(decode_table)
        return decoded
        
class Cipher(object):
    pass