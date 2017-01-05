# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:29:47 2016

@author: Ken
"""

#==============================================================================
#   Given a DNA strand GCTA must return CGAU
#   No need to invert transcription 
#==============================================================================
def to_rna(dna_seq):
    rna_dict = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna = [rna_dict[char] for char in dna_seq]
    return ''.join(char for char in rna)