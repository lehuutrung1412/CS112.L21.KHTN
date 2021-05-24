from math import gcd

a = int(input())
b = int(input())
c = int(input())
d = int(input())

def reduce(a, b):
    c = gcd(a, b)
    return a//c, b//c

count = 0
while (a != c or b != d):
    if a/b > c/d:
        count = 0
        break
    count += 1
    a, b = reduce(a+1, b+1)

print(count)