import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(*a)