import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
last_magnet = 0
count = 0
for i in range(n):
    this_magnet = int(input())
    if this_magnet != last_magnet:
        count += 1
    last_magnet = this_magnet
print(count)