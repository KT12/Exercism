# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:03:00 2016

@author: Ken
"""

#==============================================================================
#   Write a program that will calculate the date that 
#   someone will celebrate their 1 Gs anniversary.
#   Gigasecond = 10**9 seconds
#   Accuracy to the second
#==============================================================================

from datetime import timedelta

def add_gigasecond(date):
    return date + timedelta(seconds=10**9)
