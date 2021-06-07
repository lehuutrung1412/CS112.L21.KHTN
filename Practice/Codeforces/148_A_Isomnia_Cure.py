import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
count = d
for i in range(1, d+1):
    if (i % k != 0) and (i % l != 0) and (i % m != 0) and (i % n != 0):
        count -= 1
print(count)