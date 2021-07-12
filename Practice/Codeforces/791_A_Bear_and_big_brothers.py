import math
a, b = map(int, input().split())
print(int(math.log(b/a, 3/2)) + 1)