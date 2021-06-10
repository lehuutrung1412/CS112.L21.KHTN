import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
a = list(map(int, input().split()))
min_idx = max_idx = 0
min_val = max_val = a[0]
for i in range(1, n):
    if a[i] > max_val:
        max_val = a[i]
        max_idx = i
    if a[i] <= min_val:
        min_val = a[i]
        min_idx = i
if max_idx > min_idx:
    print(max_idx + n-1 - min_idx - 1)
else:
    print(max_idx + n-1 - min_idx)