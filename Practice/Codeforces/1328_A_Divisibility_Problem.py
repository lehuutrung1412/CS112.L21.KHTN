import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(b-(a%b)) if a % b != 0 else print(0)