import math
t = int(input())

def findNearestPowerOfTwo(n):
    p = int(math.log(n, 2))
    return int(pow(2, p))

for i in range(t):
    n = int(input())
    print(findNearestPowerOfTwo(n) - 1)
    