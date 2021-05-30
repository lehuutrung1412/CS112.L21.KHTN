import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
if n & 1:
    print(n//2 - n)
else:
    print(n//2)