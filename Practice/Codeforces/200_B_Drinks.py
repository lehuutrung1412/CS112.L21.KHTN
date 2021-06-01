import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
p = list(map(int, input().split()))
print(sum(p)/n)