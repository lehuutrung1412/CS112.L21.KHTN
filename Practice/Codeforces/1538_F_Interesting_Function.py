import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    count = 0
    while (l != 0 or r != 0):
        count += r - l
        r //= 10
        l //= 10
    print(count)