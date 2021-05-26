import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, k = map(int, input().split())
half = n // 2
if n & 1: 
    half += 1
if k <= half:
    print(2*k-1)
else:
    print((k - half) * 2)