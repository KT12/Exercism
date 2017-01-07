#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:08:10 2017

@author: ktt
"""

from string import ascii_lowercase
from random import choice

c = ascii_lowercase[3:] + ascii_lowercase[:3]
encode_table = str.maketrans(ascii_lowercase, c)
decode_table = str.maketrans(c, ascii_lowercase)

class Caesar(object):
    
    def __init__(self):
        pass
    
    def filter(self, phrase):
        return ''.join([c.lower() for c in phrase if c.isalpha()])
        
    def encode(self, phrase):
        ph = self.filter(phrase)
        cipher = ph.translate(encode_table)
        return ''.join(cipher.split())
    
    def decode(self, ph):
        decoded = ph.translate(decode_table)
        return decoded
        
class Cipher(object):
    
    def __init__(self, key=None):
        if not key:
            key = ''.join(choice(ascii_lowercase) for k in range(100))
        elif not key.isalpha() or not key.islower():
            raise ValueError('All items in the key must be chars and lowercase!')
        self.key = key
    
    def filter(self, phrase):
        return ''.join([ch.lower() for ch in phrase if ch.isalpha()])    
    
    def encode(self, text):
        text_lower = self.filter(text)
        key = self.key * (len(text_lower) // len(self.key) + 1)
        return ''.join(chr((ord(ch) - 194 + ord(k)) % 26 + 97)
                       for ch, k in zip(text_lower, key))
    
    def decode(self, encoded):
        key = self.key * (len(encoded) // len(self.key) + 1)
        return ''.join(chr((ord(ch) - ord(k) + 26) % 26 + 97)
                       for ch, k in zip(encoded, key))
