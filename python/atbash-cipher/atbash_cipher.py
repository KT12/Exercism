# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 15:00:09 2016

@author: Ken
"""

#==============================================================================
#   Implement the atbash cipher, an ancient encryption system
#   created in the Middle East.  The Atbash cipher is a simple substitution 
#   cipher that relies on transposing all the letters in the alphabet such that
#   the resulting alphabet is backwards. 
#
#==============================================================================

from string import punctuation

alph = 'abcdefghijklmnopqrstuvwxyz'
# Reverse the alphabet for cipher
teba = alph[::-1]

def encode(msg):
     # Punctuation ignored in cipher
    cipher = str.maketrans(alph, teba, punctuation)
    # Lowercase, remove whitespace
    secret = msg.lower().replace(' ','').translate(cipher)
    #insert spaces every 5 letters
    return ' '.join(secret[n:n+5] for n in range(0, len(secret), 5))

def decode(secret):
    rev_cipher = str.maketrans(teba, alph)
    return secret.lower().replace(' ','').translate(rev_cipher)