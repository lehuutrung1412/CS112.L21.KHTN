import math

t = int(input())

def isPerfectSquare(x):
    sqrt_x = int(math.sqrt(x))
    return ((sqrt_x*sqrt_x) == x)

def check_sub_perfect(a):
    for j in a:
        if not isPerfectSquare(j):
            return 'YES'
    return 'NO'

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(check_sub_perfect(a))
    