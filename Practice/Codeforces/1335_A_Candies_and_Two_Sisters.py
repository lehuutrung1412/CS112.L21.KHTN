import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input())
for _ in range(t):
    n = int(input())
    print((n-1)//2)