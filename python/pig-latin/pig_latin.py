#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 22:11:08 2017

@author: ktt
"""

def translate(phrase):
    ph = ''
    for st in phrase.split(' '):
        ph = ph + ' ' + trans(st)
    return ph.strip()


def trans(st):
        vowels = 'aeiouy'
        if st[0] == 'y' and st[1] in vowels:
            return st[1:] + st[0] + 'ay'
        elif st[0] in vowels:
            return st + 'ay'
        elif st[:2] == 'qu':
            return st[2:] + 'quay'
        elif st[0] not in vowels and st[1:3] == 'qu':
            return st[3:] + st[0] + 'quay'
        elif st[:2] == 'xr':
            return st + 'ay'
        elif st[0] not in vowels and st[1] not in vowels and st[2] not in vowels:
            return st[3:] + st[:3] + 'ay'
        elif st[0] not in vowels and st[1] not in vowels:
            return st[2:] + st[0:2] + 'ay'
        else:
            return st[1:] + st[0] + 'ay'