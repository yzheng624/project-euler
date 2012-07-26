'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

prime = [2, 3, 5, 7, 11, 13, 17, 19]

def factor(i):
    for p in prime:
        if p == 0:
            break
        elif i % p == 0:
            n = 0
            while i % p == 0:
                n = n + 1
                i = i / p
            yield [p, n]

if __name__ == "__main__":
    a = []
    for i in range(1, 21):
        l = factor(i)
        for e in l:
            for k in a:
                if e[0] == k[0]:
                    k[1] = max(e[1], k[1])
                    break
            else:
                a.append(e)
    ans = 1
    for i in a:
        ans = ans * (i[0] ** i[1])
    print ans