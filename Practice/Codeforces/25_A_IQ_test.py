import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
lst = list(map(lambda x: int(x) & 1, input().split()))
even = lst.count(0)
print(lst.index(0)+1) if even < n-even else print(lst.index(1)+1)