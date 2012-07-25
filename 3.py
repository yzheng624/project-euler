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