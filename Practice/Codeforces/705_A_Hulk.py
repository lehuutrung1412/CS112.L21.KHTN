import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
s = ''
for i in range(n):
    if i & 1:
        s += 'I love'
    else:
        s += 'I hate'
    if i == n-1:
        s += ' it'
    else:
        s += ' that '
print(s)