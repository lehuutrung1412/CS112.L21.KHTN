import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
p = set(p[1:])
p |= set(q[1:])
if len(p) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')