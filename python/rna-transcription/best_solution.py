# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:48:30 2016

@author: Ken
"""

# Best solution on Exercism 

def to_rna(text):
	trans = str.maketrans('GCTA', 'CGAU')
	return text.translate(trans)
