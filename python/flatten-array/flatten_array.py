#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:43:13 2017

@author: ktt
"""

def flatten(py_list):
    flat = []
    for k in py_list:
        if k not in [None, (), [], {}]:
            if isinstance(k, list):
                flat.extend(flatten(k))
            else:
                flat.append(k)
    return flat