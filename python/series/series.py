# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:34:53 2016

@author: Ken
"""
#==============================================================================
#   Write a program that will take a string of digits and give you 
#   all the contiguous substrings of length n in that string.
#==============================================================================

def slices(digits, n):
    if n > len(digits) or n == 0:
        raise ValueError
    else:
        output = []
        suboutput = []
        iterations = len(digits) - n + 1 # 
        for k in range(0, iterations):
#            output.append(int(digits[k:(n+k)]))
#        return output
            series = str(digits[k:(n+k)])
            [suboutput.append(int(num)) for num in series]
            output.append(suboutput)
            suboutput = []
        return output