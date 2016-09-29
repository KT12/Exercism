# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:10:40 2016

@author: Ken
"""

#==============================================================================
#   Write a program that, given a number, can find the sum of all the multiples 
#   of particular numbers up to but not including that number.
#==============================================================================

def sum_of_multiples(n, factors):
    # factors is ascending list of natural numbers
    # Iff 0 is in the list, it will be the first element
    if factors[0] == 0:
        factors = factors[1:] # Unsure if this is faster than factors.remove(0)
    # set will remove duplicate factors - not stated clearly in instrux
    return sum(set(k for k in range(n) for f in factors if k%f == 0))