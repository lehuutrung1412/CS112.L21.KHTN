import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, m = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
min_ = 999999999
for i in range(n-1, m):
    min_ = min(min_, f[i] - f[i-n+1])
print(min_)