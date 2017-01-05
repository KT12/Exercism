# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:30:46 2016

@author: Ken
"""

#==============================================================================
# Struggled as sorted() does not always return same ordered string
# ALso, there has to be a better way to check German pangrams...
#==============================================================================

def is_pangram(text_string):
    if 'ö' in text_string:
        german_check = 'abbcddefghijklmnopqrstuvwxyzßäöü'
        txt = ''.join(char for char in set(text_string) if char.isalpha()).lower()
        if sorted(german_check) == sorted(txt):
            return True
        else:
            return False
            
    else:
       check = 'abcdefghijklmnopqrstuvwxyz'
       txt = ''.join(char for char in set(text_string) if char.isalpha()).lower()
       if sorted(check) == sorted(txt):
           return True
       else:
           return False
