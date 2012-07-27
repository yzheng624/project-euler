'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
try:
    for i in range(1000, 333, -1):
        for j in range(1000 - i, 0, -1):
            k = 1000 - i - j
            if i ** 2 == (j ** 2) + (k ** 2) and k != 0:
                print i * j * k
                raise StopIteration
except StopIteration:
    pass
