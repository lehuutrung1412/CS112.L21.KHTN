import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
color = set(map(int, input().split()))
print(4 - len(color))