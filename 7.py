'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math
import numpy

def prime(upto):
    '''list of primes under upto'''
    return [2] + filter(lambda num: (num % numpy.arange(3, 1 + int(math.sqrt(num)), 2)).all(),
                        range(3, int(upto) + 1, 2))

print prime(110000)[10000]