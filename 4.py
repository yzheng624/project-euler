# -*- coding: utf-8 -*-
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

try:
    for i in range(999, 99, -1):
        n = int(str(i) + ''.join(i for i in reversed(str(i))))
        for j in range(999, 99, -1):
            if n / j > 1000:
                continue
            elif n / j < 100:
                break
            elif n % j == 0:
                print n, j, n/j
                raise StopIteration()
except StopIteration:
    pass
