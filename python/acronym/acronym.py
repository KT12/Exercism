# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 18:00:13 2016

@author: Ken
"""

#==============================================================================
#   Convert a long phrase to its acronym
#
#   Figuring out the camelCase regex took a little tinkering.
#==============================================================================

import re

def  abbreviate(phr):
    uncamel = re.sub(r'(.)([A-Z][a-z]+)', r'\1 \2', phr)
    uncamel2 = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', uncamel)
    no_punc = re.sub(r':|;|,|\.|_|-|\'|"|\s', r' ', uncamel2)
    return ''.join(word[0].upper() for word in no_punc.split())