# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 22:44:14 2016

@author: Ken
"""

def is_leap_year(year):
    # Input is year
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True