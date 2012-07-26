'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def square(val):
    return val * val

def sum_of_squre(n):
    l = [square(i) for i in xrange(1, n+1)]
    return sum(l)

def square_of_sum(n):
    l = [i for i in xrange(1, n+1)]
    return square(sum(l))

if __name__ == '__main__':
    print sum_of_squre(100) - square_of_sum(100)