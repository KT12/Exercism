# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:51:03 2016

@author: Ken
"""

def distance(dna_seq1, dna_seq2):
    if len(dna_seq1) != len(dna_seq2):
        raise ValueError('DNA sequences not of equal length.')
    ham_dist = 0
    for k in range(len(dna_seq1)):
        if dna_seq1[k] != dna_seq2[k]:
            ham_dist += 1
    return ham_dist