# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:22:56 2016

@author: Ken
"""

import re

def word_count(phrase):
    pattern = re.compile('[_\W]+')
    cleanlist = re.sub(pattern, ' ', phrase).lower()
    w_dict = {}
    for word in cleanlist.split():
        if word in w_dict.keys():
            w_dict[word] += 1
        else:
            w_dict[word] = 1
    return w_dict

# Instead of re.findall, used re.sub and removed what was not necessary