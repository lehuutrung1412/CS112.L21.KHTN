import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    if total == n:
        print(0)
    elif total > n:
        print(total - n)
    else:
        print(1)