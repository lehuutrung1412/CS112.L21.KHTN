import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
a = int(input())
b = int(input())
c = int(input())
res = []
res.append((a + b) * c)
res.append(a * b + c)
res.append(a + b * c)
res.append(a * (b + c))
res.append(a * b * c)
res.append(a + b + c)
print(max(res))