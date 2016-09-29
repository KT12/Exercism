# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 00:45:05 2016

@author: Ken
"""

#==============================================================================
#   Implement the Sieve of Eratosthenes
#==============================================================================

'''

Unfortunately, primes pulls in an additional set of prime divisors every time 
the algorithm runs.  I tried unsuccessfully to fix the code.

Instead, the final return has list(set()) to remove duplicates.

'''

import math

def recur_sieve(dividend, divisors, primes=[2]): # 2 is prime
    if len(divisors) == 0:
        return sorted(list(set(primes + dividend)))
    else:
        primes.append(divisors[0])
        dividend = [num for num in dividend if num % divisors[0]]
        divisors = [num for num in divisors if num % divisors[0]]
        return recur_sieve(dividend, divisors, primes)

def sieve(num):
    # Assume all even numbers not prime    
    dividend = list(range(3, num + 1, 2))
    divisors = list(range(3, int(math.sqrt(num + 5)) + 2, 2)) #margin of error
    return recur_sieve(dividend, divisors)