'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

import numpy
import math

def prime(upto):
    return [2] + filter(lambda num: (num % numpy.arange(3, 1 + int(math.sqrt(num)), 2)).all(), 
                        range(3, int(upto) + 1, 2))

print sum(prime(2e6))