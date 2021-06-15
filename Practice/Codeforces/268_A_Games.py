import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
home = []
guest = []
for _ in range(n):
    h, g = map(int, input().split())
    home.append(h)
    guest.append(g)
count = 0
for h in home:
    for g in guest:
        if h == g:
            count += 1
print(count)