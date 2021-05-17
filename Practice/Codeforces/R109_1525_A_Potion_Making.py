from math import gcd

def reduce(a, b):
    c = gcd(a, b)
    return a//c, b//c

t = int(input())
for i in range(t):
    k = int(input())
    _, res = reduce(k, 100)
    print(res)