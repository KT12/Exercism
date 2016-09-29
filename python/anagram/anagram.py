# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 01:59:06 2016

@author: Ken
"""

#==============================================================================
#
#   Write a program that, given a word and a list of possible anagrams,
#    selects the correct sublist.
#
#   Given `"listen"` and a list of candidates like `"enlists" "google"
#   "inlets" "banana"` the program should return a list containing
#   `"inlets"`.
#
#==============================================================================

def detect_anagrams(word, candidates_list):
    candidates_list = [item for item in candidates_list if item.lower() != word.lower()]
    return [an for an in candidates_list if sorted(str(an).lower()) == sorted(word.lower())]
    
#==============================================================================
#    Originally had below for loop instead of list comp to remove same words,
#    but it didn't remove 'Go' correctly.
#
#    for palabra in candidates_list:
#        print(palabra.lower())
#        if palabra.lower() == word.lower():
#            candidates_list.remove(palabra)
#            print(candidates_list)     
#==============================================================================
